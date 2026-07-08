import streamlit as st


def render_notification_settings():
    st.markdown("### 🔔 Notification Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.toggle("Enable Email Alerts", value=True)
        st.toggle("Enable Critical Error Alerts", value=True)
        st.toggle("Enable Cost Threshold Alerts", value=True)

    with col2:
        st.text_input("Alert Email", value="admin@sentinel.ai")
        st.number_input("Cost Alert Threshold ($)", value=50, min_value=1)
        st.number_input("Latency Alert Threshold (ms)", value=1500, min_value=100)

    st.divider()