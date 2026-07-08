import plotly.graph_objects as go
import streamlit as st


GREEN = "#22C55E"
GOLD = "#D97706"
DARK = "#111827"
MUTED = "#475569"
GRID = "#E5E7EB"


def _render_chart(fig, key):
    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True,
            key=key,
            config={"displayModeBar": False},
        )


def render_provider_comparison():

    providers = ["Ollama", "Groq", "Gemini"]

    avg_latency = [620, 280, 740]
    p95_latency = [1120, 640, 1310]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=providers,
            y=avg_latency,
            name="Average",
            marker_color=GREEN,
            text=avg_latency,
            textposition="outside",
        )
    )

    fig.add_trace(
        go.Bar(
            x=providers,
            y=p95_latency,
            name="P95",
            marker_color=GOLD,
            text=p95_latency,
            textposition="outside",
        )
    )

    fig.update_layout(
        title=dict(
            text="Provider Latency Comparison",
            x=0.03,
            xanchor="left",
            font=dict(
                family="Inter",
                size=18,
                color=DARK,
            ),
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Inter",
            size=13,
            color=DARK,
        ),
        height=340,
        margin=dict(
            l=25,
            r=20,
            t=55,
            b=20,
        ),
        barmode="group",
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
            font=dict(
                color=MUTED,
                size=11,
            ),
        ),
        autosize=True,
    )

    fig.update_xaxes(
        showgrid=False,
        showline=True,
        linewidth=1,
        linecolor="#CBD5E1",
        tickfont=dict(
            color=MUTED,
            size=11,
        ),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        gridwidth=1,
        showline=True,
        linewidth=1,
        linecolor="#CBD5E1",
        tickfont=dict(
            color=MUTED,
            size=11,
        ),
    )

    _render_chart(
        fig,
        key="provider_latency_comparison",
    )