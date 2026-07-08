import streamlit as st


def render_system_recommendations():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("System Health Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.success("CPU and memory usage are currently within a healthy range.")
        st.warning("Vector Store latency is elevated. Check indexing workload and cache usage.")

    with col2:
        st.info("Disk usage is stable but should be monitored as logs grow.")
        st.success("Core monitoring services are operating normally.")

    st.markdown("</div>", unsafe_allow_html=True)