import streamlit as st


def render_provider_settings():
    st.markdown("### 🤖 AI Provider Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.selectbox(
            "Default Provider",
            [
                "Ollama",
                "Groq",
                "Gemini",
                "OpenAI",
            ],
        )

        st.toggle("Enable Automatic Provider Failover", value=True)

        st.toggle("Enable Provider Health Monitoring", value=True)

    with col2:
        st.number_input(
            "Request Timeout (seconds)",
            value=30,
            min_value=5,
            max_value=120,
        )

        st.number_input(
            "Maximum Retries",
            value=3,
            min_value=0,
            max_value=10,
        )

    st.divider()