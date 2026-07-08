import streamlit as st


def render_error_recommendations():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Error Resolution Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.warning("Timeout errors are increasing on /summarize. Review prompt length and provider latency.")
        st.info("Rate limit errors suggest request throttling should be added.")

    with col2:
        st.error("Provider failures on Gemini should be monitored closely.")
        st.success("Validation errors are low and mostly resolved.")

    st.markdown("</div>", unsafe_allow_html=True)