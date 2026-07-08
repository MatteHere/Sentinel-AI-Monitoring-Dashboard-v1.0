import pandas as pd
import streamlit as st


def render_cost_table():
    df = pd.DataFrame(
        {
            "Request ID": [
                "req_8f7d2a1c",
                "req_4b6e91d2",
                "req_9c3d2f1b",
                "req_1a2b3c4d",
                "req_7e6f5a4b",
            ],
            "Provider": ["Gemini", "Groq", "Ollama", "Gemini", "Groq"],
            "Model": [
                "gemini-1.5-pro",
                "llama-3.1-70b",
                "llama3",
                "gemini-1.5-flash",
                "mixtral",
            ],
            "Tokens": ["12,840", "8,320", "3,920", "9,110", "6,740"],
            "Cost": ["$0.082", "$0.046", "$0.000", "$0.031", "$0.027"],
            "Endpoint": ["/summarize", "/chat", "/quiz", "/sql", "/sentiment"],
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Expensive Requests")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)