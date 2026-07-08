import streamlit as st

from ui.components import metric_card


def render_system_metrics():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "CPU Usage",
            "46%",
            "-3%",
            "🖥️",
        )

    with col2:
        metric_card(
            "Memory Usage",
            "47%",
            "-2%",
            "💾",
        )

    with col3:
        metric_card(
            "Disk Usage",
            "64%",
            "+1%",
            "🗄️",
        )

    with col4:
        metric_card(
            "System Uptime",
            "99.98%",
            "Healthy",
            "✅",
        )