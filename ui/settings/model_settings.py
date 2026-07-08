import streamlit as st


def render_model_settings():
    st.markdown("### 🧠 Model Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.selectbox(
            "Default Model",
            [
                "llama3",
                "mixtral",
                "gemini-1.5-flash",
                "gemini-1.5-pro",
                "gpt-4o-mini",
            ],
        )

        st.slider("Temperature", 0.0, 1.0, 0.7)

        st.number_input(
            "Max Output Tokens",
            value=2048,
            min_value=256,
            max_value=8192,
        )

    with col2:
        st.toggle("Enable Response Streaming", value=True)
        st.toggle("Enable Token Tracking", value=True)
        st.toggle("Enable Cost Tracking", value=True)

    st.divider()