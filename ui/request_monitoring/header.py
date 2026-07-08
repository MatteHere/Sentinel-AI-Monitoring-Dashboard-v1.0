from datetime import datetime

import streamlit as st


def render_request_header():
    left, right = st.columns([4.2, 1])

    with left:
        st.markdown(
            """
            <div class="page-header-title">Request Monitoring</div>
            <div class="page-header-subtitle">
                Track AI request history, latency, status, token usage, cost, and provider performance.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            f"""
            <div class="live-card">
                <div>
                    <span class="live-dot"></span>
                    <span class="live-text">Live</span>
                </div>
                <div class="last-updated">Last Updated</div>
                <div class="last-updated">{datetime.now().strftime("%I:%M:%S %p")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )