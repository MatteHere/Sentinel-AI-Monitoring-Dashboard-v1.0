import streamlit as st

from ui.error_monitoring.charts import render_error_charts
from ui.error_monitoring.metrics import render_error_metrics
from ui.error_monitoring.error_table import render_error_table
from ui.error_monitoring.recommendations import render_error_recommendations


def render_error_monitoring():
    st.markdown(
        """
        <div class="page-header-title">Error Monitoring</div>
        <div class="page-header-subtitle">
            Monitor failed requests, AI provider failures, exceptions, timeout issues, and application stability in real time.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_error_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_error_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_error_table()

    st.markdown("<br>", unsafe_allow_html=True)

    render_error_recommendations()