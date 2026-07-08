import streamlit as st


def render_request_details():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Request Details")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Request ID**")
        st.code("req_8f7d2a1c")

        st.markdown("**Provider**")
        st.write("Ollama")

        st.markdown("**Model**")
        st.write("llama3")

        st.markdown("**Latency**")
        st.write("842 ms")

        st.markdown("**Status**")
        st.success("Success")

    with col2:
        st.markdown("**Tokens**")
        st.write("1,280")

        st.markdown("**Estimated Cost**")
        st.write("$0.004")

        st.markdown("**Endpoint**")
        st.write("/chat")

        st.markdown("**Timestamp**")
        st.write("2026-07-03 11:42:10")

        st.markdown("**Trace ID**")
        st.code("trace_f82ab4719")

    st.markdown("---")

    st.markdown("### Prompt")

    st.code(
        "Explain Retrieval Augmented Generation with an example.",
        language="text",
    )

    st.markdown("### AI Response")

    st.info(
        "Retrieval-Augmented Generation (RAG) combines external knowledge retrieval with large language models to generate accurate and context-aware responses..."
    )

    st.markdown("</div>", unsafe_allow_html=True)