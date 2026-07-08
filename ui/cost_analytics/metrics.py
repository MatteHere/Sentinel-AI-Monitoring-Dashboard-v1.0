import streamlit as st

from ui.components import metric_card


def render_cost_metrics():
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Total Spend", "$169.42", "11.8%", "💰")

    with c2:
        metric_card("Avg Cost / Request", "$0.0068", "4.2%", "📊")

    with c3:
        metric_card("Highest Cost Model", "Gemini", "7.5%", "🧠")

    with c4:
        metric_card("Monthly Forecast", "$742", "13.1%", "📈")