import streamlit as st


def stat_card(title, value, subtitle):
    st.markdown(
        f"""
        <div class="system-card">
            <div class="system-title">{title}</div>
            <div class="system-value">{value}</div>
            <div style="font-size:13px;opacity:0.8;">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_bottom_statistics():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        stat_card(
            "Avg Prompt Length",
            "642",
            "characters",
        )

    with col2:
        stat_card(
            "Avg Completion",
            "1,124",
            "tokens",
        )

    with col3:
        stat_card(
            "Cache Hit Rate",
            "81.6%",
            "last 24 hrs",
        )

    with col4:
        stat_card(
            "Retry Rate",
            "2.8%",
            "automatic retries",
        )