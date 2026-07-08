import pandas as pd
import streamlit as st


def render_endpoint_latency_table():
    df = pd.DataFrame(
        {
            "Endpoint": ["/chat", "/summarize", "/sql", "/sentiment", "/quiz"],
            "Avg Latency": ["284 ms", "742 ms", "1.12 s", "418 ms", "690 ms"],
            "P95": ["640 ms", "1.24 s", "1.86 s", "830 ms", "1.31 s"],
            "P99": ["1.12 s", "2.04 s", "2.71 s", "1.44 s", "2.10 s"],
            "Requests": ["12,840", "8,420", "4,910", "6,230", "5,710"],
            "Error Rate": ["0.8%", "1.6%", "2.4%", "1.1%", "1.9%"],
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Endpoint Latency Breakdown")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)