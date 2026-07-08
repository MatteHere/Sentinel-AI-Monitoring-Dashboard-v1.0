import pandas as pd
import streamlit as st

from services.reporting.export_service import (
    dataframe_to_csv,
    dataframe_to_excel,
    generate_pdf_report,
)


def render_export_panel():
    st.success("NEW REPORT EXPORT PANEL LOADED")
    st.markdown('<div class="table-card">', unsafe_allow_html=True)

    st.subheader("Export Center")

    # Sample export data
    df = pd.DataFrame(
        {
            "Metric": [
                "Requests",
                "Latency (ms)",
                "Errors",
                "Cost ($)",
                "Tokens",
            ],
            "Value": [
                18420,
                342,
                18,
                32.44,
                1543200,
            ],
        }
    )

    # Generate downloadable files
    pdf_data = generate_pdf_report()
    csv_data = dataframe_to_csv(df)
    excel_data = dataframe_to_excel(df)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="📄 Download PDF",
            data=pdf_data,
            file_name="sentinel_report.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="download_pdf_report",
        )

    with col2:
        st.download_button(
            label="📊 Download CSV",
            data=csv_data,
            file_name="sentinel_report.csv",
            mime="text/csv",
            use_container_width=True,
            key="download_csv_report",
        )

    with col3:
        st.download_button(
            label="📈 Download Excel",
            data=excel_data,
            file_name="sentinel_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
            key="download_excel_report",
        )

    st.caption(
        "Export the current dashboard summary as PDF, CSV, or Excel."
    )

    st.markdown("</div>", unsafe_allow_html=True)