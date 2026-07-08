import streamlit as st


def render_request_insights():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("💡 Request Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
🔥 **Busiest Provider:** Groq

⚡ **Fastest Model:** llama3

💰 **Highest Cost Model:** Gemini 1.5 Pro
"""
        )

    with col2:
        st.info(
            """
🐢 **Slowest Endpoint:** /summarize

❌ **Most Common Error:** Timeout

📈 **Peak Traffic:** 10:20 AM
"""
        )

    st.markdown("</div>", unsafe_allow_html=True)