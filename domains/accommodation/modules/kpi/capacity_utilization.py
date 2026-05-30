import pandas as pd


# ============================================
# CAPACITY UTILIZATION
# ============================================

def calculate_capacity_utilization(df):

    df["capacity_utilization"] = (
        df["active_bookings"] /
        df["maximum_capacity"]
    )

    return df


# ============================================
# AVERAGE UTILIZATION
# ============================================

def get_average_utilization(df):

    return (
        df["capacity_utilization"]
        .mean()
    )