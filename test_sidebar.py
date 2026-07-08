import streamlit as st

st.set_page_config(
    page_title="Sidebar Test",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("🛡️ Sentinel AI")
page = st.sidebar.radio(
    "Navigation",
    ["Executive Dashboard", "Request Monitoring", "Settings"]
)

st.title(page)
st.write("If you can see this sidebar, Streamlit sidebar is working.")