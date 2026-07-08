import streamlit as st

from services.database.alert_service import get_alerts


def render_active_alerts():
    df = get_alerts()

    if df.empty:
        st.warning("No active alerts available.")
        return

    df = df.rename(
        columns={
            "title": "Alert",
            "severity": "Severity",
            "status": "Status",
            "created_at": "Created",
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Active Alerts")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)