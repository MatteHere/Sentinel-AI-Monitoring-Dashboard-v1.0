import streamlit as st


def render_export_center():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Export Center")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button("Export CSV", use_container_width=True)

    with col2:
        st.button("Export Excel", use_container_width=True)

    with col3:
        st.button("Export JSON", use_container_width=True)

    with col4:
        st.button("Generate Report", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)