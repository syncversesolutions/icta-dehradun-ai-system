import pandas as pd


# ============================================
# BOOKING VELOCITY
# ============================================

def calculate_booking_velocity(df):

    df["booking_velocity"] = (
        df["new_bookings"] /
        df["time_interval"]
    )

    return df


# ============================================
# AVERAGE BOOKING VELOCITY
# ============================================

def get_average_booking_velocity(df):

    return (
        df["booking_velocity"]
        .mean()
    )