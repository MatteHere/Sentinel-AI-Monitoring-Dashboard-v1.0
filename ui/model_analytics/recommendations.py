import streamlit as st


def render_model_recommendations():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Model Optimization Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Groq has the lowest average latency. Use it for real-time workloads.")
        st.info("Ollama has zero API cost. Use it for local/offline testing.")

    with col2:
        st.warning("Gemini has the highest latency and cost. Use it only for quality-critical tasks.")
        st.info("OpenAI and Claude provide balanced reliability for production workflows.")

    st.markdown("</div>", unsafe_allow_html=True)