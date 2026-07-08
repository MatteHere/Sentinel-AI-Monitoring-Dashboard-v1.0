import pandas as pd
import streamlit as st


def render_alert_rules():
    df = pd.DataFrame(
        {
            "Rule": [
                "High Latency",
                "Critical Error Spike",
                "Provider Failure",
                "Cost Threshold",
                "Disk Usage Warning",
            ],
            "Condition": [
                "P95 latency > 1500 ms",
                "Critical errors > 5 in 10 min",
                "Provider failures > 3",
                "Daily cost > $50",
                "Disk usage > 80%",
            ],
            "Severity": [
                "Warning",
                "Critical",
                "Critical",
                "Warning",
                "Warning",
            ],
            "Status": [
                "Enabled",
                "Enabled",
                "Enabled",
                "Enabled",
                "Disabled",
            ],
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Alert Rules")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)