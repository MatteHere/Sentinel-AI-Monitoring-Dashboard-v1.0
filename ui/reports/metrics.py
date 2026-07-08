import streamlit as st

from ui.components import metric_card


def render_report_metrics():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Reports Generated", "42", "8.1%", "📄")

    with col2:
        metric_card("Exports Today", "16", "3.4%", "📥")

    with col3:
        metric_card("Scheduled Reports", "7", "+2", "📅")

    with col4:
        metric_card("Success Rate", "99.2%", "1.1%", "✅")