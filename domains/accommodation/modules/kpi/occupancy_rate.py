import pandas as pd


# ============================================
# OCCUPANCY RATE
# ============================================

def calculate_occupancy_rate(df):

    df["occupancy_rate"] = (
        df["occupied_rooms"] /
        df["total_rooms"]
    )

    return df


# ============================================
# AVERAGE OCCUPANCY
# ============================================

def get_average_occupancy(df):

    return (
        df["occupancy_rate"]
        .mean()
    )