import streamlit as st


def render_cost_recommendations():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Cost Optimization Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Use Groq for high-volume low-cost workloads.")
        st.info("Cache repeated prompts to reduce token spend.")

    with col2:
        st.warning("Gemini Pro is driving the highest request cost.")
        st.warning("Large summaries are increasing completion token usage.")

    st.markdown("</div>", unsafe_allow_html=True)