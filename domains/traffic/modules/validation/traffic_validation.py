# ============================================
# IMPORTS
# ============================================

import pandas as pd

# ============================================
# VALIDATE TRAFFIC DATA
# ============================================

def validate_traffic_data(df):

    print(df)
    print("\nStarting traffic validation...")

    print("\nInitial Shape:")
    print(df.shape)

    # ============================================
    # REQUIRED COLUMNS
    # ============================================

    required_columns = [

        "calendar_date",
        "route_id",
        "checkpoint_name",
        "vehicle_count",
        "congestion_level",
        "crowd_density"
    ]

    # ============================================
    # CHECK MISSING COLUMNS
    # ============================================

    missing_columns = [

        col for col in required_columns
        if col not in df.columns
    ]

    if len(missing_columns) > 0:

        raise ValueError(
            f"Missing required columns: "
            f"{missing_columns}"
        )

    # ============================================
    # REMOVE DUPLICATES
    # ============================================

    before_duplicates = len(df)

    df = df.drop_duplicates()

    print(
        f"\nRemoved duplicates: "
        f"{before_duplicates - len(df)}"
    )

    # ============================================
    # DATE VALIDATION
    # ============================================

    df["calendar_date"] = pd.to_datetime(

        df["calendar_date"],
        errors="coerce"
    )

    before_dates = len(df)

    df = df.dropna(
        subset=["calendar_date"]
    )

    print(
        f"\nRemoved invalid dates: "
        f"{before_dates - len(df)}"
    )

    # ============================================
    # NUMERIC VALIDATION
    # ============================================

    df["vehicle_count"] = pd.to_numeric(

        df["vehicle_count"],
        errors="coerce"
    )

    before_numeric = len(df)

    df = df.dropna(
        subset=["vehicle_count"]
    )

    print(
        f"\nRemoved invalid throughput rows: "
        f"{before_numeric - len(df)}"
    )

    # ============================================
    # REMOVE NEGATIVE VALUES
    # ============================================

    before_negative = len(df)

    df = df[
        df["vehicle_count"] >= 0
    ]

    print(
        f"\nRemoved negative throughput rows: "
        f"{before_negative - len(df)}"
    )

    # ============================================
    # STANDARDIZE TEXT COLUMNS
    # ============================================

    text_columns = [

        "route_id",
        "checkpoint_name",
        "congestion_level"
    ]

    for col in text_columns:

        df[col] = (

            df[col]
            .astype(str)
            .str.strip()
        )

    # ============================================
    # STANDARDIZE CONGESTION LEVEL
    # ============================================

    df["congestion_level"] = (

        df["congestion_level"]
        .str.title()
    )

    # ============================================
    # VALID CONGESTION LEVELS
    # ============================================

    valid_levels = [

        "Low",
        "Medium",
        "High",
        "Severe"
    ]

    before_levels = len(df)

    df = df[
        df["congestion_level"]
        .isin(valid_levels)
    ]

    print(
        f"\nRemoved invalid congestion levels: "
        f"{before_levels - len(df)}"
    )

    # ============================================
    # RESET INDEX
    # ============================================

    df = df.reset_index(
        drop=True
    )

    # ============================================
    # FINAL DEBUG
    # ============================================

    print("\nFinal Shape:")
    print(df.shape)

    print("\nValidated Dataset Sample:")
    print(df.head())

    return df