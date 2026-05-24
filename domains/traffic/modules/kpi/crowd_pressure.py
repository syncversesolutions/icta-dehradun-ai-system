def calculate_crowd_pressure(df):

    df["crowd_pressure"] = (
        df["crowd_density"] *
        df["vehicle_count"]
    )

    return df


def get_avg_crowd_pressure(df):

    return df["crowd_pressure"].mean()