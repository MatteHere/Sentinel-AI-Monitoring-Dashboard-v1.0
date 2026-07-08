import plotly.graph_objects as go
import streamlit as st

from services.latency_data import get_latency_data


GREEN = "#22C55E"
GOLD = "#D97706"
RED = "#EF4444"
DARK = "#111827"
MUTED = "#475569"
GRID = "#E5E7EB"


def _chart_layout(title):
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
        hoverlabel=dict(bgcolor="#FFFFFF", bordercolor=GRID, font=dict(color=DARK)),
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


def render_latency_charts():
    df = get_latency_data()
    left, right = st.columns(2)

    with left:
        fig = go.Figure()

        for name, column, color in [
            ("P50", "p50", GREEN),
            ("P95", "p95", GOLD),
            ("P99", "p99", RED),
        ]:
            fig.add_trace(
                go.Scatter(
                    x=df["time"],
                    y=df[column],
                    name=name,
                    mode="lines+markers",
                    line=dict(color=color, width=4, shape="spline"),
                    marker=dict(
                        size=8,
                        color=color,
                        line=dict(color="#FFFFFF", width=2),
                    ),
                )
            )

        fig.update_layout(**_chart_layout("Latency Percentiles"))
        _style_axes(fig)

        _render_chart(fig, "latency_percentiles_chart")

    with right:
        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=df["time"],
                y=df["requests"],
                name="Requests",
                marker_color=GREEN,
            )
        )

        fig.update_layout(**_chart_layout("Requests Processed"))
        _style_axes(fig)

        _render_chart(fig, "latency_requests_chart")