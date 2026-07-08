import plotly.graph_objects as go
import streamlit as st


GREEN = "#22C55E"
GOLD = "#D97706"
RED = "#EF4444"
BLUE = "#2563EB"
DARK = "#111827"
MUTED = "#475569"
GRID = "#E5E7EB"


def _base_layout(title, height=340):
    return dict(
        title=dict(
            text=title,
            x=0.03,
            xanchor="left",
            font=dict(family="Inter", size=18, color=DARK),
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Inter", size=13, color=DARK),
        height=height,
        margin=dict(l=25, r=20, t=55, b=20),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor=GRID,
            font=dict(color=DARK, size=13),
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.03,
            xanchor="right",
            x=1,
            bgcolor="rgba(255,255,255,0)",
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


def _chart_key(title):
    return (
        title.lower()
        .replace(" ", "_")
        .replace(".", "")
        .replace("(", "")
        .replace(")", "")
        .replace("%", "percent")
    )


def _render_chart(fig, key):
    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True,
            key=key,
            config={"displayModeBar": False},
        )


def line_chart(df, y_column, title, color):
    final_color = color

    if color in ["#6EE782", "#28D665"]:
        final_color = GREEN

    if color in ["#FF5A4F"]:
        final_color = RED

    fill_color = (
        "rgba(34,197,94,0.12)"
        if final_color == GREEN
        else "rgba(239,68,68,0.10)"
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df[y_column],
            mode="lines+markers",
            line=dict(color=final_color, width=4, shape="spline"),
            marker=dict(
                size=8,
                color=final_color,
                line=dict(width=2, color="#FFFFFF"),
            ),
            fill="tozeroy",
            fillcolor=fill_color,
            hovertemplate="%{x}<br>%{y}<extra></extra>",
        )
    )

    fig.update_layout(**_base_layout(title, height=340))
    _style_axes(fig)

    _render_chart(fig, key=f"{_chart_key(title)}_chart")


def latency_chart(df):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["p50"],
            name="P50",
            mode="lines+markers",
            line=dict(color=GREEN, width=4, shape="spline"),
            marker=dict(size=8, color=GREEN, line=dict(color="#FFFFFF", width=2)),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["p95"],
            name="P95",
            mode="lines+markers",
            line=dict(color=GOLD, width=4, shape="spline"),
            marker=dict(size=8, color=GOLD, line=dict(color="#FFFFFF", width=2)),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["p99"],
            name="P99",
            mode="lines+markers",
            line=dict(color=RED, width=4, shape="spline"),
            marker=dict(size=8, color=RED, line=dict(color="#FFFFFF", width=2)),
        )
    )

    fig.update_layout(**_base_layout("Latency Distribution", height=340))
    _style_axes(fig)

    _render_chart(fig, key="dashboard_latency_chart")


def model_donut_chart():
    labels = ["Ollama", "Groq", "Gemini", "Other"]
    values = [35, 30, 25, 10]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.58,
                textinfo="label+percent",
                textfont=dict(color=DARK, size=12),
                marker=dict(
                    colors=[GREEN, GOLD, BLUE, RED],
                    line=dict(color="#FFFFFF", width=1),
                ),
                hovertemplate="%{label}<br>%{percent}<extra></extra>",
            )
        ]
    )

    fig.update_layout(**_base_layout("Requests by Model", height=340))
    fig.update_layout(
        showlegend=False,
        margin=dict(l=10, r=10, t=55, b=10),
    )

    _render_chart(fig, key="dashboard_model_chart")