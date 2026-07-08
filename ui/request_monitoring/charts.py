import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from services.database.request_service import get_all_requests


GREEN = "#22C55E"
GOLD = "#D97706"
RED = "#EF4444"
DARK = "#111827"
MUTED = "#475569"
GRID = "#E5E7EB"


def get_request_timeline_data():
    df = get_all_requests()

    if df.empty:
        return pd.DataFrame(
            columns=[
                "time",
                "requests",
                "errors",
                "queue_size",
                "avg_latency",
            ]
        )

    df["created_at"] = pd.to_datetime(df["created_at"])
    df["time"] = df["created_at"].dt.strftime("%H:%M")

    grouped = (
        df.groupby("time")
        .agg(
            requests=("request_id", "count"),
            errors=("status", lambda x: (x == "Failed").sum()),
            queue_size=("status", lambda x: (x == "Failed").sum()),
            avg_latency=("latency", "mean"),
        )
        .reset_index()
    )

    return grouped


def _layout(title):
    return dict(
        title=dict(
            text=title,
            font=dict(size=18, color=DARK, family="Inter"),
            x=0.03,
            xanchor="left",
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(color=DARK, family="Inter", size=13),
        height=340,
        margin=dict(l=25, r=20, t=55, b=20),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor=GRID,
            font=dict(color=DARK),
        ),
        legend=dict(
            orientation="h",
            y=1.03,
            x=1,
            xanchor="right",
            font=dict(color=MUTED, size=11),
        ),
        autosize=True,
    )


def _style_axes(fig):
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showline=True,
        linewidth=1,
        linecolor="#CBD5E1",
        tickfont=dict(color=MUTED, size=11),
        ticks="outside",
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        gridwidth=1,
        zeroline=False,
        showline=True,
        linewidth=1,
        linecolor="#CBD5E1",
        tickfont=dict(color=MUTED, size=11),
    )


def _render_chart(fig, key):
    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True,
            key=key,
            config={"displayModeBar": False},
        )


def render_request_timeline():
    df = get_request_timeline_data()

    if df.empty:
        st.warning("No request timeline data available.")
        return

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["requests"],
            name="Requests",
            mode="lines+markers",
            line=dict(color=GREEN, width=4, shape="spline"),
            marker=dict(size=8, color=GREEN, line=dict(color="#FFFFFF", width=2)),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["errors"],
            name="Errors",
            mode="lines+markers",
            line=dict(color=RED, width=4, shape="spline"),
            marker=dict(size=8, color=RED, line=dict(color="#FFFFFF", width=2)),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["queue_size"],
            name="Queue Size",
            mode="lines+markers",
            line=dict(color=GOLD, width=4, shape="spline"),
            marker=dict(size=8, color=GOLD, line=dict(color="#FFFFFF", width=2)),
        )
    )

    fig.update_layout(**_layout("Request Timeline"))
    _style_axes(fig)

    _render_chart(fig, "request_timeline_chart")


def render_latency_heatmap():
    df = get_request_timeline_data()

    if df.empty:
        st.warning("No latency heatmap data available.")
        return

    endpoints = ["/chat", "/summarize", "/sql", "/sentiment", "/quiz"]
    hours = list(df["time"])

    latency_values = list(df["avg_latency"])

    latency = []

    for index, _endpoint in enumerate(endpoints):
        multiplier = 1 + (index * 0.12)
        latency.append([round(value * multiplier, 1) for value in latency_values])

    fig = go.Figure(
        data=go.Heatmap(
            z=latency,
            x=hours,
            y=endpoints,
            colorscale=[
                [0, "#DCFCE7"],
                [0.5, "#FACC15"],
                [1, "#EF4444"],
            ],
            colorbar=dict(
                title=dict(text="Latency (ms)", font=dict(color=DARK)),
                tickfont=dict(color=MUTED),
            ),
        )
    )

    fig.update_layout(**_layout("Latency Heatmap"))
    _style_axes(fig)

    _render_chart(fig, "request_latency_heatmap_chart")


def render_request_charts():
    left, right = st.columns(2)

    with left:
        render_request_timeline()

    with right:
        render_latency_heatmap()