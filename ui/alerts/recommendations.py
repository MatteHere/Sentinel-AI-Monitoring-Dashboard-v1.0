import streamlit as st


def render_alert_recommendations():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Alert Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.warning("Latency alerts are increasing. Review slow endpoints and provider response times.")
        st.info("Enable throttling rules for repeated timeout spikes.")

    with col2:
        st.error("Gemini provider failure alerts need priority investigation.")
        st.success("Cost threshold alerts are under control after recent optimization.")

    st.markdown("</div>", unsafe_allow_html=True)