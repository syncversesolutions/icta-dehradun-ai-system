import streamlit as st

from ui.cards.metric_card import render_metric_card
from ui.cards.alert_card import render_alert
from ui.cards.ai_card import render_ai_card

from ui.charts.congestion_chart import render_congestion_chart
from ui.maps.traffic_map import render_traffic_map


def render_traffic_dashboard(state, alerts, recommendations):

    st.title("Traffic Command Center")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card(
            "Congestion",
            f"{state['traffic']['congestion'] * 100:.0f}%"
        )

    with col2:
        render_metric_card(
            "Vehicle Density",
            f"{state['traffic']['vehicle_density'] * 100:.0f}%"
        )

    with col3:
        render_metric_card(
            "Travel Delay",
            f"{state['traffic']['travel_delay']} mins"
        )

    with col4:
        render_metric_card(
            "Checkpoint Throughput",
            f"{state['traffic']['checkpoint_throughput']}%"
        )

    col_left, col_right = st.columns([2, 1])

    with col_left:
        render_traffic_map()

        st.plotly_chart(
            render_congestion_chart(),
            use_container_width=True
        )

    with col_right:

        st.subheader("Alerts")

        for alert in alerts:
            render_alert(alert)

        st.subheader("AI Recommendations")

        for rec in recommendations:
            render_ai_card(rec)