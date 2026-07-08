import streamlit as st

from services.database.request_service import get_all_requests


def render_request_table():
    df = get_all_requests()

    if df.empty:
        st.warning("No request data available.")
        return

    df = df.rename(
        columns={
            "request_id": "Request ID",
            "provider": "Provider",
            "model": "Model",
            "latency": "Latency (ms)",
            "tokens": "Tokens",
            "cost": "Cost ($)",
            "status": "Status",
            "created_at": "Timestamp",
        }
    )

    display_columns = [
        "Timestamp",
        "Request ID",
        "Provider",
        "Model",
        "Latency (ms)",
        "Tokens",
        "Cost ($)",
        "Status",
    ]

    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.markdown("### Live Request History")
    st.dataframe(df[display_columns], use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)