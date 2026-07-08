import pandas as pd
import streamlit as st


def render_dashboard_tables():
    alerts = pd.DataFrame(
        {
            "Alert": [
                "High Latency Detected",
                "Error Rate Increased",
                "High Token Usage",
                "Cost Threshold Approaching",
            ],
            "Severity": ["Warning", "Critical", "Info", "Warning"],
            "Source": ["Ollama", "Groq", "Gemini", "System"],
            "Message": [
                "P95 latency is above 2000ms",
                "Error rate is above 2%",
                "Token usage increased by 30%",
                "Daily cost is 80% of threshold",
            ],
            "Time": ["10:21 AM", "10:18 AM", "10:15 AM", "10:12 AM"],
        }
    )

    slowest = pd.DataFrame(
        {
            "Request ID": [
                "req_8f7d2a1c",
                "req_4b6e91d2",
                "req_9c3d2f1b",
                "req_1a2b3c4d",
                "req_7e6f5a4b",
            ],
            "Model": ["Ollama", "Groq", "Gemini", "Ollama", "Groq"],
            "Latency": ["4,562 ms", "3,982 ms", "3,421 ms", "3,120 ms", "2,985 ms"],
            "Time": ["10:22 AM", "10:21 AM", "10:20 AM", "10:19 AM", "10:18 AM"],
        }
    )

    col1, col2 = st.columns([1.35, 1])

    with col1:
        st.markdown('<div class="table-card">', unsafe_allow_html=True)
        st.markdown("### Recent Alerts")
        st.dataframe(alerts, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="table-card">', unsafe_allow_html=True)
        st.markdown("### Top 5 Slowest Requests")
        st.dataframe(slowest, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)