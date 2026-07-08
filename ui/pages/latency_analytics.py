import streamlit as st

from ui.latency_analytics.charts import render_latency_charts
from ui.latency_analytics.endpoint_table import render_endpoint_latency_table
from ui.latency_analytics.metrics import render_latency_metrics
from ui.latency_analytics.provider_comparison import render_provider_comparison
from ui.latency_analytics.recommendations import render_latency_recommendations


def render_latency_analytics():
    st.markdown(
        """
        <div class="page-header-title">Latency Analytics</div>
        <div class="page-header-subtitle">
            Analyze response times, latency percentiles, endpoint performance,
            provider-level delays, and API performance trends.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Executive Metrics
    render_latency_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts
    render_latency_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    # Endpoint Performance Table
    render_endpoint_latency_table()

    st.markdown("<br>", unsafe_allow_html=True)

    # Provider Comparison
    render_provider_comparison()

    st.markdown("<br>", unsafe_allow_html=True)

    # Latency Recommendations
    render_latency_recommendations()