# =========================================================
# ICTA AI COMMAND CENTER
# =========================================================
# =========================================================
# SYSTEM PATH SETUP
# =========================================================
import sys
PROJECT_ROOT = (
    "/content/drive/MyDrive/project_cd"
)
sys.path.append(PROJECT_ROOT)
# =========================================================
# IMPORTS
# =========================================================
import json
from datetime import datetime
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import (
    st_autorefresh
)
from config.paths import PATHS
# =========================================================
# THEME IMPORTS
# =========================================================
from ui.themes.dark_theme import (
    apply_theme as apply_dark_theme
)
from ui.themes.light_theme import (
    apply_theme as apply_light_theme
)
# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="ICTA AI Command Center",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =========================================================
# THEME SWITCHER
# =========================================================
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Dark"
theme_mode = st.sidebar.selectbox(
    "Theme",
    [
        "Dark",
        "Light"
    ]
)
st.session_state.theme_mode = theme_mode
# =========================================================
# APPLY THEME
# =========================================================
if theme_mode == "Dark":
    st.markdown(
        apply_dark_theme(),
        unsafe_allow_html=True
    )
else:
    st.markdown(
        apply_light_theme(),
        unsafe_allow_html=True
    )
# =========================================================
# AUTO REFRESH
# =========================================================
st_autorefresh(
    interval=30000,
    key="dashboard_refresh"
)
# =========================================================
# HEADER
# =========================================================
st.title(
    "ICTA Dehradun AI Command Center"
)
st.markdown(
    "Realtime Strategic Operations Intelligence Platform"
)
# =========================================================
# LOAD SYSTEM STATE
# =========================================================
system_state_path = (
    PATHS["system"]["state"] +
    "system_state.json"
)
with open(
    system_state_path,
    "r"
) as file:
    system_state = json.load(file)
# =========================================================
# LOAD DATA PATHS
# =========================================================
traffic_path = (
    PATHS["traffic"]["validated"] +
    "validated_traffic.csv"
)
features_path = (
    PATHS["traffic"]["features"] +
    "traffic_features.csv"
)
prediction_path = (
    PATHS["traffic"]["predictions"] +
    "traffic_predictions.csv"
)
alerts_path = (
    PATHS["system"]["ai"] +
    "active_alerts.json"
)
impact_path = (
    PATHS["system"]["graph"] +
    "impact_analysis.json"
)
# =========================================================
# READ DATA
# =========================================================
traffic_df = pd.read_csv(
    traffic_path
)
features_df = pd.read_csv(
    features_path
)
prediction_df = pd.read_csv(
    prediction_path
)
with open(
    alerts_path,
    "r"
) as file:
    alerts = json.load(file)
with open(
    impact_path,
    "r"
) as file:
    impacts = json.load(file)
# =========================================================
# GLOBAL METRICS
# =========================================================
total_vehicles = (
    traffic_df["vehicle_count"]
    .sum()
)
avg_density = (
    traffic_df["crowd_density"]
    .mean()
)
total_alerts = len(alerts)
high_risk = len(
    prediction_df[
        prediction_df[
            "predicted_risk_level"
        ] == "High"
    ]
)
# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title(
    "ICTA Operations"
)
st.sidebar.markdown("---")
section = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Traffic Intelligence",
        "Predictions",
        "Impact Analysis",
        "AI Alerts",
        "Workflow",
        "Raw Data"
    ]
)
st.sidebar.markdown("---")
st.sidebar.success(
    "AI Engine Active"
)
st.sidebar.info(
    f"""
    Last Pipeline Run:
    {system_state['last_pipeline_run']}
    """
)
# =========================================================
# TOP METRICS
# =========================================================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        "Vehicles",
        int(total_vehicles)
    )
with col2:
    st.metric(
        "Crowd Density",
        round(avg_density, 2)
    )
with col3:
    st.metric(
        "Active Alerts",
        total_alerts
    )
with col4:
    st.metric(
        "High Risk Routes",
        high_risk
    )
st.markdown("---")
# =========================================================
# CHART TEMPLATE
# =========================================================
chart_template = (
    "plotly_dark"
    if theme_mode == "Dark"
    else "plotly_white"
)
# =========================================================
# OVERVIEW
# =========================================================
if section == "Overview":
    st.header(
        "Strategic Operations Overview"
    )
    left, right = st.columns([2, 1])
    # =====================================================
    # LEFT PANEL
    # =====================================================
    with left:
        fig = px.bar(
            traffic_df,
            x="checkpoint_name",
            y="vehicle_count",
            color="congestion_level",
            title="Vehicle Distribution"
        )
        fig.update_layout(
            template=chart_template
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
        heatmap = px.density_heatmap(
            traffic_df,
            x="checkpoint_name",
            y="crowd_density",
            title="Crowd Density Heatmap"
        )
        heatmap.update_layout(
            template=chart_template
        )
        st.plotly_chart(
            heatmap,
            use_container_width=True
        )
    # =====================================================
    # RIGHT PANEL
    # =====================================================
    with right:
        st.subheader(
            "AI Recommendations"
        )
        st.markdown("""
        <div class="ai-card">
        <b>Restrict Inflow</b>
        <br><br>
        High congestion predicted
        near Kedarnath route.
        <br><br>
        Impact:
        Reduce downstream saturation
        </div>
        """, unsafe_allow_html=True)
        st.subheader(
            "System Status"
        )
        st.json(system_state)
# =========================================================
# TRAFFIC INTELLIGENCE
# =========================================================
elif section == "Traffic Intelligence":
    st.header(
        "Traffic Intelligence"
    )
    fig = px.bar(
        traffic_df,
        x="checkpoint_name",
        y="vehicle_count",
        color="congestion_level",
        title="Vehicle Count by Checkpoint"
    )
    fig.update_layout(
        template=chart_template
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    scatter = px.scatter(
        traffic_df,
        x="vehicle_count",
        y="crowd_density",
        color="congestion_level",
        size="vehicle_count",
        hover_data=[
            "checkpoint_name"
        ],
        title="Traffic Pressure Analysis"
    )
    scatter.update_layout(
        template=chart_template
    )
    st.plotly_chart(
        scatter,
        use_container_width=True
    )
# =========================================================
# PREDICTIONS
# =========================================================
elif section == "Predictions":
    st.header(
        "AI Predictions"
    )
    fig = px.scatter(
        prediction_df,
        x="vehicle_count",
        y="predicted_congestion_score",
        color="predicted_risk_level",
        hover_data=[
            "checkpoint_name"
        ],
        title="Predicted Congestion Risk"
    )
    fig.update_layout(
        template=chart_template
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.dataframe(
        prediction_df,
        use_container_width=True
    )
# =========================================================
# IMPACT ANALYSIS
# =========================================================
elif section == "Impact Analysis":
    st.header(
        "Dependency Impact Analysis"
    )
    st.json(
        impacts
    )
# =========================================================
# AI ALERTS
# =========================================================
elif section == "AI Alerts":
    st.header(
        "AI Alert Center"
    )
    for alert in alerts:
        st.markdown(f"""
        <div class="alert-card">
        <b>ALERT</b>
        <br><br>
        {alert}
        </div>
        """, unsafe_allow_html=True)
# =========================================================
# WORKFLOW
# =========================================================
elif section == "Workflow":
    st.header(
        "Operational Workflow"
    )
    st.markdown("""
    ### System Intelligence Flow
    RAW DATA
        ↓
    VALIDATION
        ↓
    KPI ENGINEERING
        ↓
    FEATURE ENGINEERING
        ↓
    PREDICTION
        ↓
    SIGNAL GENERATION
        ↓
    SIGNAL AGGREGATION
        ↓
    IMPACT ANALYSIS
        ↓
    AI ALERTING
        ↓
    GLOBAL STATE UPDATE
        ↓
    COMMAND CENTER
    """)
# =========================================================
# RAW DATA
# =========================================================
elif section == "Raw Data":
    st.header(
        "Raw Data Explorer"
    )
    dataset = st.selectbox(
        "Select Dataset",
        [
            "Traffic",
            "Features",
            "Predictions"
        ]
    )
    if dataset == "Traffic":
        st.dataframe(
            traffic_df,
            use_container_width=True
        )
    elif dataset == "Features":
        st.dataframe(
            features_df,
            use_container_width=True
        )
    elif dataset == "Predictions":
        st.dataframe(
            prediction_df,
            use_container_width=True
        )
# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption(
    f"""
    ICTA AI Operations Platform
    | Last Refresh:
    {datetime.now().strftime('%H:%M:%S')}
    """
)