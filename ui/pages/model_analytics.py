import streamlit as st

from ui.model_analytics.charts import render_model_charts
from ui.model_analytics.metrics import render_model_metrics
from ui.model_analytics.model_table import render_model_table
from ui.model_analytics.recommendations import render_model_recommendations


def render_model_analytics():
    st.markdown(
        """
        <div class="page-header-title">Model Analytics</div>
        <div class="page-header-subtitle">
            Compare AI model performance, latency, cost, token usage, reliability, and request volume.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_model_metrics()

    st.markdown("<br>", unsafe_allow_html=True)

    render_model_charts()

    st.markdown("<br>", unsafe_allow_html=True)

    render_model_table()

    st.markdown("<br>", unsafe_allow_html=True)

    render_model_recommendations()