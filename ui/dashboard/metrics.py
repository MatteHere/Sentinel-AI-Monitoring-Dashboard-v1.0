import streamlit as st

from services.database.dashboard_service import get_dashboard_metrics
from services.database.error_service import get_errors
from ui.components import metric_card


def _format_tokens(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"

    if value >= 1_000:
        return f"{value / 1_000:.1f}K"

    return str(value)


def render_executive_metrics():
    metrics = get_dashboard_metrics()
    errors = get_errors()

    total_errors = len(errors)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        metric_card(
            "Total Requests",
            f"{metrics['total_requests']:,}",
            "Live",
            "📦",
        )

    with col2:
        metric_card(
            "Success Rate",
            f"{metrics['success_rate']:.2f}%",
            "Live",
            "✅",
        )

    with col3:
        metric_card(
            "Avg. Latency",
            f"{metrics['avg_latency']:.0f} ms",
            "Live",
            "⏱️",
        )

    with col4:
        metric_card(
            "Total Tokens",
            _format_tokens(metrics["total_tokens"]),
            "Live",
            "🧱",
        )

    with col5:
        metric_card(
            "Est. Cost",
            f"${metrics['total_cost']:.2f}",
            "Live",
            "💰",
        )

    with col6:
        metric_card(
            "Total Errors",
            str(total_errors),
            "Live",
            "⚠️",
        )