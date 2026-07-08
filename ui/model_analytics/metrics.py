import streamlit as st

from ui.components import metric_card


def render_model_metrics():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Total Models",
            "6",
            "1 New",
            "🤖",
        )

    with col2:
        metric_card(
            "Active Requests",
            "24,581",
            "12.4%",
            "⚡",
        )

    with col3:
        metric_card(
            "Best Performer",
            "Groq",
            "Lowest Latency",
            "🏆",
        )

    with col4:
        metric_card(
            "Avg Success Rate",
            "98.8%",
            "0.9%",
            "✅",
        )