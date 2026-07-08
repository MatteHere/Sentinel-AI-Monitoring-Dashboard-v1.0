import streamlit as st

from services.demo_data import create_demo_data
from ui.dashboard.analytics import render_analytics
from ui.dashboard.header import render_header
from ui.dashboard.metrics import render_executive_metrics
from ui.dashboard.system_health import render_system_health
from ui.dashboard.tables import render_dashboard_tables


def render_executive_dashboard():
    df = create_demo_data()

    render_header()
    render_executive_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_analytics(df)

    st.markdown("<br>", unsafe_allow_html=True)

    render_system_health()

    st.markdown("<br>", unsafe_allow_html=True)

    render_dashboard_tables()