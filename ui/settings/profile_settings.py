import streamlit as st


def render_profile_settings():
    st.markdown("### 👤 Profile Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Admin Name", value="Admin")
        st.text_input("Organization", value="Sentinel AI")
        st.text_input("Role", value="System Administrator")

    with col2:
        st.text_input("Email", value="admin@sentinel.ai")
        st.selectbox("Timezone", ["Asia/Kolkata", "UTC", "America/New_York", "Europe/London"])
        st.toggle("Enable Activity Logs", value=True)

    st.divider()