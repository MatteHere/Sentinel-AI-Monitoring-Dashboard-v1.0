import streamlit as st

from ui.reports.charts import render_report_charts
from ui.reports.metrics import render_report_metrics
from ui.reports.history_table import render_report_history
from ui.reports.export_panel import render_export_panel


def render_reports():
    st.markdown(
        """
        <div class="page-header-title">Reports</div>
        <div class="page-header-subtitle">
            Generate AI monitoring reports, export analytics, schedule reports, and review historical system performance.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_report_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_report_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_report_history()

    st.markdown("<br>", unsafe_allow_html=True)

    render_export_panel()