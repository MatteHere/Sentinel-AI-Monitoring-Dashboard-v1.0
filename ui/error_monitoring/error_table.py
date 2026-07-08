import streamlit as st

from services.database.error_service import get_errors


def render_error_table():
    df = get_errors()

    if df.empty:
        st.warning("No error logs available.")
        return

    df = df.rename(
        columns={
            "request_id": "Request ID",
            "error_type": "Error Type",
            "severity": "Severity",
            "message": "Message",
            "created_at": "Time",
        }
    )

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Recent Error Logs")
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)