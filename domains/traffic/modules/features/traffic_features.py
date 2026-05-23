import pandas as pd


def create_traffic_features(df):

    # ============================================
    # VEHICLE DENSITY RATIO
    # ============================================

    df["vehicle_density_ratio"] = (

        df["vehicle_count"] /

        (df["crowd_density"] + 1)
    )

    # ============================================
    # CROWD TRAFFIC INTERACTION
    # ============================================

    df["crowd_vehicle_interaction"] = (

        df["crowd_density"] *

        df["vehicle_count"]
    )

    # ============================================
    # HIGH CONGESTION FLAG
    # ============================================

    df["high_congestion_flag"] = (

        df["congestion_score"] >= 3
    ).astype(int)

    # ============================================
    # DAY OF WEEK
    # ============================================

    df["calendar_date"] = pd.to_datetime(
        df["calendar_date"]
    )

    df["day_of_week"] = (
        df["calendar_date"]
        .dt.dayofweek
    )

    # ============================================
    # WEEKEND FLAG
    # ============================================

    df["is_weekend"] = (
        df["day_of_week"] >= 5
    ).astype(int)

    return df