import streamlit as st


def render_latency_recommendations():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("AI Latency Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Groq is currently the fastest provider. Route low-latency workloads there.")
        st.warning("The /sql endpoint has elevated P95 latency. Review query generation prompts.")

    with col2:
        st.info("Enable caching for repeated prompts to reduce average latency.")
        st.warning("Gemini shows higher tail latency during peak traffic windows.")

    st.markdown("</div>", unsafe_allow_html=True)