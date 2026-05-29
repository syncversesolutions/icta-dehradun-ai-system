from dashboards.overview.overview_dashboard import render_overview_dashboard
from dashboards.traffic.traffic_dashboard import render_traffic_dashboard


def route_dashboard(page, state, alerts, recommendations):

    if page == "Overview":

        render_overview_dashboard(state)

    elif page == "Traffic":

        render_traffic_dashboard(
            state,
            alerts,
            recommendations
        )