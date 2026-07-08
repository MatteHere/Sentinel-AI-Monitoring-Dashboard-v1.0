from io import BytesIO

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def dataframe_to_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


def dataframe_to_excel(df: pd.DataFrame, sheet_name="Report") -> bytes:
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)

    return output.getvalue()


def generate_pdf_report() -> bytes:
    output = BytesIO()

    pdf = canvas.Canvas(output, pagesize=A4)
    width, height = A4

    pdf.setTitle("Sentinel AI Report")

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, height - 60, "Sentinel AI Monitoring Report")

    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, height - 90, "Generated from Sentinel AI Dashboard")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 140, "Executive Summary")

    pdf.setFont("Helvetica", 11)

    summary_lines = [
        "Total Requests: 18,420",
        "Average Latency: 342 ms",
        "Total Errors: 18",
        "Estimated Cost: $32.44",
        "Total Tokens: 1,543,200",
    ]

    y = height - 170

    for line in summary_lines:
        pdf.drawString(70, y, line)
        y -= 22

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y - 20, "Insights")

    pdf.setFont("Helvetica", 11)

    insights = [
        "System performance is stable.",
        "Latency is within acceptable monitoring limits.",
        "Error rate is low and manageable.",
        "Cost usage is under the current threshold.",
    ]

    y -= 50

    for insight in insights:
        pdf.drawString(70, y, f"- {insight}")
        y -= 22

    pdf.showPage()
    pdf.save()

    return output.getvalue()