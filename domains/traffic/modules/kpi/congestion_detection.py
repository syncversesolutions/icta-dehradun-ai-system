def calculate_congestion_score(df):

    # ============================================
    # MAP CONGESTION LEVELS TO SCORES
    # ============================================

    congestion_mapping = {

        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Severe": 4
    }

    df["congestion_score"] = (
        df["congestion_level"]
        .map(congestion_mapping)
    )

    return df


def get_avg_congestion(df):

    return df["congestion_score"].mean()