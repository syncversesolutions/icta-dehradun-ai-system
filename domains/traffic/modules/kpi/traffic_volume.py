def calculate_traffic_volume(df):

    df["traffic_volume"] = (
        df["vehicle_count"]
    )

    return df


def get_avg_traffic_volume(df):

    return df["traffic_volume"].mean()