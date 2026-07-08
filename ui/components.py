import streamlit as st


def metric_card(label, value, change, icon):
    """
    Displays a custom executive metric card.

    label: metric name
    value: main value
    change: comparison text
    icon: visual icon for the card
    """
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{icon} {label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-change">↑ {change} vs last 7 days</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def page_header(title, subtitle):
    """
    Displays the page title and page subtitle.
    """
    st.markdown(f'<div class="title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{subtitle}</div>', unsafe_allow_html=True)