import streamlit as st

from ui.settings.provider_settings import render_provider_settings
from ui.settings.model_settings import render_model_settings
from ui.settings.notification_settings import render_notification_settings
from ui.settings.database_settings import render_database_settings
from ui.settings.profile_settings import render_profile_settings


def render_settings():
    st.markdown(
        """
        <div class="page-header-title">Settings</div>
        <div class="page-header-subtitle">
            Configure dashboard preferences, AI providers, models, notifications, database connections, and application settings.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_provider_settings()

    st.markdown("<br>", unsafe_allow_html=True)

    render_model_settings()

    st.markdown("<br>", unsafe_allow_html=True)

    render_notification_settings()

    st.markdown("<br>", unsafe_allow_html=True)

    render_database_settings()

    st.markdown("<br>", unsafe_allow_html=True)

    render_profile_settings()
