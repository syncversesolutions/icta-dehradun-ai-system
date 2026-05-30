import pandas as pd


# ============================================
# CHECK-IN FLOW
# ============================================

def calculate_checkin_flow(df):

    df["checkin_flow"] = (
        df["checkins"] /
        df["time_interval"]
    )

    return df


# ============================================
# AVERAGE CHECK-IN FLOW
# ============================================

def get_average_checkin_flow(df):

    return (
        df["checkin_flow"]
        .mean()
    )