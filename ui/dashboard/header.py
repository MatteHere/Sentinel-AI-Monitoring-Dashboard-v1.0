from datetime import datetime

import streamlit as st


def render_header():
    left, right = st.columns([4.2, 1])

    with left:
        st.markdown(
            """
            <div class="page-header-title">Executive Dashboard</div>
            <div class="page-header-subtitle">
                Overview of AI application performance, latency, token usage, cost, reliability and infrastructure health.
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