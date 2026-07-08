import streamlit as st

from ui.components import metric_card


def render_latency_metrics():
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Average Latency", "842 ms", "6.2%", "⚡")

    with c2:
        metric_card("P95 Latency", "1.12 s", "3.8%", "📈")

    with c3:
        metric_card("P99 Latency", "1.92 s", "2.1%", "🚀")

    with c4:
        metric_card("Slow Requests", "428", "1.9%", "🐢")