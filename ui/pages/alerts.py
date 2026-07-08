import streamlit as st

from ui.alerts.charts import render_alert_charts
from ui.alerts.metrics import render_alert_metrics
from ui.alerts.active_alerts import render_active_alerts
from ui.alerts.rules import render_alert_rules
from ui.alerts.recommendations import render_alert_recommendations


def render_alerts():
    st.markdown(
        """
        <div class="page-header-title">Alerts</div>
        <div class="page-header-subtitle">
            Monitor active incidents, critical notifications, provider outages, latency spikes, and automated alert rules.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_alert_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_alert_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_active_alerts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_alert_rules()

    st.markdown("<br>", unsafe_allow_html=True)

    render_alert_recommendations()