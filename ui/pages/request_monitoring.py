import streamlit as st

from ui.request_monitoring.bottom_stats import render_bottom_statistics
from ui.request_monitoring.charts import render_request_charts
from ui.request_monitoring.details import render_request_details
from ui.request_monitoring.export import render_export_center
from ui.request_monitoring.filters import render_request_filters
from ui.request_monitoring.header import render_request_header
from ui.request_monitoring.metrics import render_request_metrics
from ui.request_monitoring.request_insights import render_request_insights
from ui.request_monitoring.request_table import render_request_table
from ui.request_monitoring.demo_logger import render_demo_logger
from ui.request_monitoring.traffic_controls import render_traffic_controls


def render_request_monitoring():
    render_request_header()

    st.markdown("<br>", unsafe_allow_html=True)

    render_request_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_request_filters()

    st.markdown("<br>", unsafe_allow_html=True)

    render_request_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_request_insights()

    st.markdown("<br>", unsafe_allow_html=True)

    render_demo_logger()

    st.markdown("<br>", unsafe_allow_html=True)

    render_traffic_controls()

    st.markdown("<br>", unsafe_allow_html=True)

    render_request_table()

    st.markdown("<br>", unsafe_allow_html=True)

    render_request_details()

    st.markdown("<br>", unsafe_allow_html=True)

    render_export_center()

    st.markdown("<br>", unsafe_allow_html=True)

    render_bottom_statistics()