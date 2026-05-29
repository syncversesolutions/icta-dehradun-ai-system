import streamlit as st
from ui.cards.metric_card import render_metric_card


def render_overview_dashboard(state):

    st.title("Strategic Operations Center")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card("System Health", "92%")

    with col2:
        render_metric_card("Occupancy", "84%")

    with col3:
        render_metric_card("Flow Efficiency", "76%")

    with col4:
        render_metric_card("Active Alerts", "3")

    st.info(
        "AI Operational Intelligence Engine Active"
    )