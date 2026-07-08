import pandas as pd
import streamlit as st


def render_service_table():
    df = pd.DataFrame(
        {
            "Service": [
                "AI Gateway",
                "Request Logger",
                "SQLite Database",
                "Vector Store",
                "Monitoring Engine",
                "Export Service",
            ],
            "Status": [
                "Healthy",
                "Healthy",
                "Healthy",
                "Warning",
                "Healthy",
                "Healthy",
            ],
            "Uptime": [
                "99.99%",
                "99.98%",
                "99.96%",
                "98.42%",
                "99.91%",
                "99.89%",
            ],
            "Latency": [
                "22 ms",
                "18 ms",
                "9 ms",
                "140 ms",
                "31 ms",
                "45 ms",
            ],
            "Last Checked": [
                "Now",
                "Now",
                "Now",
                "1 min ago",
                "Now",
                "Now",
            ],
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Service Status")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)