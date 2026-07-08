import plotly.graph_objects as go
import streamlit as st

from ui.cost_analytics.data import get_cost_data


GREEN = "#22C55E"
GOLD = "#D97706"
RED = "#EF4444"
BLUE = "#2563EB"
DARK = "#111827"
MUTED = "#475569"
GRID = "#E5E7EB"


def _layout(title):
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
        height=340,
        margin=dict(l=25, r=20, t=55, b=20),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor=GRID,
            font=dict(color=DARK, size=13),
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


def render_cost_charts():
    df = get_cost_data()

    left, right = st.columns(2)

    with left:
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df["date"],
                y=df["daily_cost"],
                name="Daily Cost",
                mode="lines+markers",
                line=dict(color=GREEN, width=4, shape="spline"),
                marker=dict(size=8, color=GREEN, line=dict(color="#FFFFFF", width=2)),
                fill="tozeroy",
                fillcolor="rgba(34,197,94,0.12)",
                hovertemplate="%{x}<br>$%{y}<extra></extra>",
            )
        )

        fig.update_layout(**_layout("Daily AI Cost Trend"))
        _style_axes(fig)
        _render_chart(fig, "cost_daily_trend_chart")

    with right:
        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=df["date"],
                y=df["tokens"],
                name="Tokens",
                marker_color=BLUE,
            )
        )

        fig.update_layout(**_layout("Token Usage by Day"))
        _style_axes(fig)
        _render_chart(fig, "cost_token_usage_chart")