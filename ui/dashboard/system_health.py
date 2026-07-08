import streamlit as st

from services.system_monitor import get_system_health


def _system_card(title, value):
    st.markdown(
        f"""
        <div class="system-card">
            <div class="system-title">{title}</div>
            <div class="system-value">{value:.1f}%</div>
            <div class="progress-bg">
                <div class="progress-fill" style="width:{value}%;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_system_health():
    health = get_system_health()

    st.markdown("## 🖥️ System Health")

    col1, col2, col3 = st.columns(3)

    with col1:
        _system_card("CPU Usage", health["cpu"])

    with col2:
        _system_card("Memory Usage", health["memory"])

    with col3:
        _system_card("Disk Usage", health["disk"])