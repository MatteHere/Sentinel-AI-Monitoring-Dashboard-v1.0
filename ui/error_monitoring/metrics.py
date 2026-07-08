import streamlit as st

from services.database.dashboard_service import get_dashboard_metrics
from services.database.error_service import get_errors
from ui.components import metric_card


def render_error_metrics():
    metrics = get_dashboard_metrics()
    errors = get_errors()

    total_errors = len(errors)
    total_requests = metrics["total_requests"]

    if total_requests == 0:
        error_rate = 0
    else:
        error_rate = (total_errors / total_requests) * 100

    if errors.empty:
        critical_errors = 0
    else:
        critical_errors = len(
            errors[
                errors["severity"].str.lower().isin(
                    ["critical", "high"]
                )
            ]
        )

    recovery_rate = (
        100
        if total_errors == 0
        else ((total_errors - critical_errors) / total_errors) * 100
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Total Errors",
            f"{total_errors:,}",
            "Live",
            "❌",
        )

    with col2:
        metric_card(
            "Error Rate",
            f"{error_rate:.2f}%",
            "Live",
            "📉",
        )

    with col3:
        metric_card(
            "Critical Errors",
            f"{critical_errors:,}",
            "Live",
            "🚨",
        )

    with col4:
        metric_card(
            "Recovery Rate",
            f"{recovery_rate:.2f}%",
            "Live",
            "✅",
        )