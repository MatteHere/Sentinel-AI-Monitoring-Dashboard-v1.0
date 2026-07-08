import streamlit as st

from services.monitoring.traffic_simulator import generate_traffic


def render_traffic_controls():
    st.markdown("### 🚦 Live Traffic Simulator")

    col1, col2 = st.columns([2, 1])

    with col1:
        batch_size = st.slider(
            "Requests to generate",
            min_value=1,
            max_value=50,
            value=10,
        )

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "Generate Traffic",
            use_container_width=True,
            type="primary",
        ):
            generated = generate_traffic(batch_size=batch_size)

            st.success(
                f"Generated {len(generated)} simulated requests."
            )

            st.rerun()