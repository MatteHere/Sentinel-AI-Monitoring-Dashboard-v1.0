import streamlit as st

from ui.cost_analytics.charts import render_cost_charts
from ui.cost_analytics.metrics import render_cost_metrics
from ui.cost_analytics.cost_table import render_cost_table
from ui.cost_analytics.recommendations import render_cost_recommendations


def render_cost_analytics():
    st.markdown(
        """
        <div class="page-header-title">Cost Analytics</div>
        <div class="page-header-subtitle">
            Track AI spending, token costs, provider billing, expensive requests, and optimization opportunities.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_cost_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_cost_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_cost_table()

    st.markdown("<br>", unsafe_allow_html=True)

    render_cost_recommendations()