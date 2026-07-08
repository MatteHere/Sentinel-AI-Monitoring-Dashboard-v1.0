import streamlit as st


def render_database_settings():
    st.markdown("### 🗄️ Database Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.selectbox(
            "Database",
            [
                "SQLite",
                "PostgreSQL",
                "MySQL",
            ],
        )

        st.text_input(
            "Database File",
            value="sentinel_ai.db",
        )

        st.toggle(
            "Enable Automatic Backups",
            value=True,
        )

    with col2:
        st.number_input(
            "Backup Interval (hours)",
            value=24,
            min_value=1,
            max_value=168,
        )

        st.toggle(
            "Enable Query Logging",
            value=True,
        )

        st.toggle(
            "Enable Database Health Checks",
            value=True,
        )

    st.divider()