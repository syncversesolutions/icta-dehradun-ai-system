# ============================================
# ICTA AI COMMAND CENTER
# ============================================

# ============================================
# SYSTEM PATH SETUP
# ============================================

import sys
import os

PROJECT_ROOT = (
    "/content/drive/MyDrive/project_cd"
)

sys.path.append(
    PROJECT_ROOT
)

# ============================================
# IMPORTS
# ============================================

import json
import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

from streamlit_autorefresh import (
    st_autorefresh
)

from config.paths import PATHS

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(

    page_title="ICTA AI Command Center",

    layout="wide"
)

# ============================================
# AUTO REFRESH
# ============================================

st_autorefresh(

    interval=30000,

    key="dashboard_refresh"
)

# ============================================
# HEADER
# ============================================

st.title(
    "ICTA Dehradun AI Command Center"
)

st.markdown(
    "Realtime Operational Intelligence Dashboard"
)

# ============================================
# LOAD DATA
# ============================================

traffic_path = (

    PATHS["traffic"]["processed"] +
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

# ============================================
# READ FILES
# ============================================

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

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title(
    "Navigation"
)

section = st.sidebar.radio(

    "Select Section",

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

# ============================================
# OVERVIEW
# ============================================

if section == "Overview":

    st.header(
        "Operational Overview"
    )

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

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Vehicles",
        int(total_vehicles)
    )

    col2.metric(
        "Avg Crowd Density",
        round(avg_density, 2)
    )

    col3.metric(
        "Active Alerts",
        total_alerts
    )

    col4.metric(
        "High Risk Routes",
        high_risk
    )

# ============================================
# TRAFFIC INTELLIGENCE
# ============================================

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

    st.plotly_chart(
        heatmap,
        use_container_width=True
    )

# ============================================
# PREDICTIONS
# ============================================

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

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        prediction_df
    )

# ============================================
# IMPACT ANALYSIS
# ============================================

elif section == "Impact Analysis":

    st.header(
        "Impact Analysis"
    )

    st.json(
        impacts
    )

# ============================================
# AI ALERTS
# ============================================

elif section == "AI Alerts":

    st.header(
        "AI Alert Center"
    )

    for alert in alerts:

        severity = alert.get(
            "severity",
            "Unknown"
        )

        st.error(

            f"""
            ALERT:
            {alert}
            """
        )

# ============================================
# WORKFLOW
# ============================================

elif section == "Workflow":

    st.header(
        "System Workflow"
    )

    st.markdown("""

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

    IMPACT ANALYSIS
        ↓

    AI ALERTING

    """)

# ============================================
# RAW DATA
# ============================================

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
            traffic_df
        )

    elif dataset == "Features":

        st.dataframe(
            features_df
        )

    elif dataset == "Predictions":

        st.dataframe(
            prediction_df
        )