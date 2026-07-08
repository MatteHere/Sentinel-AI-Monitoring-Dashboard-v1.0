import streamlit as st


def render_filter_group(title, options, key_prefix):
    st.markdown(f"#### {title}")

    row1 = st.columns(2)
    row2 = st.columns(2)

    for index, option in enumerate(options):
        row = row1 if index < 2 else row2
        col = row[index % 2]

        with col:
            button_type = "primary" if option == "All" else "secondary"
            st.button(
                option,
                key=f"{key_prefix}_{option}",
                use_container_width=True,
                type=button_type,
            )


def render_request_filters():
    st.markdown('<div class="table-card">', unsafe_allow_html=True)
    st.subheader("Filters")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_filter_group("Provider", ["All", "Ollama", "Groq", "Gemini"], "provider")

    with col2:
        render_filter_group("Status", ["All", "Success", "Failed", "Running"], "status")

    with col3:
        render_filter_group("Model", ["All", "llama3", "mixtral", "gemini"], "model")

    with col4:
        st.text_input("Search Request", placeholder="req_...")

    st.markdown("</div>", unsafe_allow_html=True)