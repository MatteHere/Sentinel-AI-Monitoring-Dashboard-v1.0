import streamlit as st

from ui.model_analytics.data import get_model_data


def render_model_table():
    df = get_model_data().copy()

    df = df.rename(
        columns={
            "model": "Model",
            "requests": "Requests",
            "latency": "Avg Latency (ms)",
            "success_rate": "Success Rate (%)",
            "cost": "Cost ($)",
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Model Performance Overview")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)