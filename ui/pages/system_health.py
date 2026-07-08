import streamlit as st

from ui.system_health.charts import render_system_charts
from ui.system_health.metrics import render_system_metrics
from ui.system_health.service_table import render_service_table
from ui.system_health.recommendations import render_system_recommendations

def render_system_health_page():
    st.markdown(
        """
        <div class="page-header-title">System Health</div>
        <div class="page-header-subtitle">
            Monitor infrastructure utilization, uptime, resource consumption, and service health in real time.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_system_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_system_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_service_table()

    st.markdown("<br>", unsafe_allow_html=True)

    render_system_recommendations()