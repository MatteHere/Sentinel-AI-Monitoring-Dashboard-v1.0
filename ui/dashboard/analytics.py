import streamlit as st

from config.theme import GREEN, RED
from ui.charts import (
    latency_chart,
    line_chart,
    model_donut_chart,
)


def render_analytics(df):
    if df.empty:
        st.warning("No monitoring data available.")
        return

    top_left, top_right, top_donut = st.columns([1.2, 1.2, 1])

    with top_left:
        line_chart(
            df,
            "requests",
            "AI Requests Over Time",
            GREEN,
        )

    with top_right:
        latency_chart(df)

    with top_donut:
        model_donut_chart()

    st.markdown("<br>", unsafe_allow_html=True)

    bottom_left, bottom_right = st.columns(2)

    with bottom_left:
        line_chart(
            df,
            "tokens",
            "Token Usage Over Time",
            GREEN,
        )

    with bottom_right:
        line_chart(
            df,
            "errors",
            "Error Rate Over Time",
            RED,
        )