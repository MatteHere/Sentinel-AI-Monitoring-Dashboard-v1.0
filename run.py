import streamlit as st
from streamlit_autorefresh import st_autorefresh

from config.app_config import APP_NAME, PAGE_ICON, PAGE_LAYOUT
from database.seed import initialize_database
from ui.pages.alerts import render_alerts
from ui.pages.cost_analytics import render_cost_analytics
from ui.pages.error_monitoring import render_error_monitoring
from ui.pages.executive_dashboard import render_executive_dashboard
from ui.pages.latency_analytics import render_latency_analytics
from ui.pages.model_analytics import render_model_analytics
from ui.pages.reports import render_reports
from ui.pages.request_monitoring import render_request_monitoring
from ui.pages.settings import render_settings
from ui.pages.system_health import render_system_health_page
from ui.styles import apply_custom_css


PAGES = [
    "Executive Dashboard",
    "Request Monitoring",
    "Latency Analytics",
    "Cost Analytics",
    "Error Monitoring",
    "Model Analytics",
    "System Health",
    "Alerts",
    "Reports",
    "Settings",
]


ICONS = {
    "Executive Dashboard": "🏠",
    "Request Monitoring": "📈",
    "Latency Analytics": "⏱️",
    "Cost Analytics": "💰",
    "Error Monitoring": "⚠️",
    "Model Analytics": "🧊",
    "System Health": "〽️",
    "Alerts": "🔔",
    "Reports": "📄",
    "Settings": "⚙️",
}


def render_sidebar():
    if "sidebar_open" not in st.session_state:
        st.session_state.sidebar_open = True

    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "Executive Dashboard"

    if st.session_state.sidebar_open:
        if st.button("◀ Collapse", use_container_width=True):
            st.session_state.sidebar_open = False
            st.rerun()

        st.markdown("## 🛡️ Sentinel AI")
        st.caption("AI Monitoring Dashboard")
        st.divider()

        for page in PAGES:
            label = f"{ICONS[page]} {page}"
            button_type = (
                "primary"
                if st.session_state.selected_page == page
                else "secondary"
            )

            if st.button(
                label,
                key=f"nav_{page}",
                use_container_width=True,
                type=button_type,
            ):
                st.session_state.selected_page = page
                st.rerun()

        st.divider()
        st.markdown("### ☀️ Theme")
        st.divider()
        st.markdown("**Admin**")
        st.caption("admin@sentinel.ai")

    else:
        if st.button("▶", use_container_width=True):
            st.session_state.sidebar_open = True
            st.rerun()

        st.markdown("## 🛡️")

        for page in PAGES:
            button_type = (
                "primary"
                if st.session_state.selected_page == page
                else "secondary"
            )

            if st.button(
                ICONS[page],
                key=f"icon_{page}",
                use_container_width=True,
                type=button_type,
            ):
                st.session_state.selected_page = page
                st.rerun()


def render_page():
    page = st.session_state.selected_page

    if page == "Executive Dashboard":
        render_executive_dashboard()

    elif page == "Request Monitoring":
        render_request_monitoring()

    elif page == "Latency Analytics":
        render_latency_analytics()

    elif page == "Cost Analytics":
        render_cost_analytics()

    elif page == "Model Analytics":
        render_model_analytics()

    elif page == "Error Monitoring":
        render_error_monitoring()

    elif page == "System Health":
        render_system_health_page()

    elif page == "Alerts":
        render_alerts()

    elif page == "Reports":
        render_reports()

    elif page == "Settings":
        render_settings()

    else:
        st.markdown(
            f'<div class="page-header-title">{page}</div>',
            unsafe_allow_html=True,
        )
        st.info("This module will be implemented next.")


def main():
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=PAGE_ICON,
        layout=PAGE_LAYOUT,
    )

    initialize_database()
    apply_custom_css()

    st_autorefresh(
        interval=5000,
        key="sentinel_auto_refresh",
    )

    sidebar_width = 1.15 if st.session_state.get("sidebar_open", True) else 0.35
    sidebar_col, content_col = st.columns([sidebar_width, 5.5], gap="small")

    with sidebar_col:
        render_sidebar()

    with content_col:
        render_page()


if __name__ == "__main__":
    main()