import streamlit as st

from services.database.alert_service import get_alerts
from ui.components import metric_card


def render_alert_metrics():
    alerts = get_alerts()

    total_alerts = len(alerts)

    if alerts.empty:
        critical_alerts = 0
        resolved_alerts = 0
    else:
        severity = alerts["severity"].astype(str).str.lower()
        status = alerts["status"].astype(str).str.lower()

        critical_alerts = len(
            alerts[
                severity.isin(["critical", "high"])
            ]
        )

        resolved_alerts = len(
            alerts[
                status == "resolved"
            ]
        )

    open_alerts = total_alerts - resolved_alerts

    # Placeholder until alert resolution timestamps are implemented
    avg_resolve_time = "18 min"

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Active Alerts",
            str(open_alerts),
            "Live",
            "🚨",
        )

    with col2:
        metric_card(
            "Critical Alerts",
            str(critical_alerts),
            "Live",
            "🔥",
        )

    with col3:
        metric_card(
            "Resolved Alerts",
            str(resolved_alerts),
            "Live",
            "✅",
        )

    with col4:
        metric_card(
            "Avg Resolve Time",
            avg_resolve_time,
            "Coming Soon",
            "⏱️",
        )