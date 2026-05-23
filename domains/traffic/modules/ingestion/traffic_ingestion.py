# ============================================
# IMPORTS
# ============================================

import pandas as pd

# ============================================
# INGEST TRAFFIC DATA
# ============================================

def ingest_traffic_data(
    checkpoint_path,
    crowd_path
):

    print("\nLoading raw datasets...")

    # ============================================
    # LOAD DATASETS
    # ============================================

    checkpoint_df = pd.read_csv(
        checkpoint_path
    )

    crowd_df = pd.read_csv(
        crowd_path
    )

    # ============================================
    # DEBUG SCHEMA
    # ============================================

    print("\nCheckpoint Dataset Columns:")
    print(checkpoint_df.columns.tolist())

    print("\nCrowd Dataset Columns:")
    print(crowd_df.columns.tolist())

    # ============================================
    # STANDARDIZE COLUMN NAMES
    # ============================================

    checkpoint_df.columns = (

        checkpoint_df.columns
        .str.strip()
        .str.lower()
    )

    crowd_df.columns = (

        crowd_df.columns
        .str.strip()
        .str.lower()
    )

    # ============================================
    # SELECT REQUIRED CHECKPOINT COLUMNS
    # ============================================

    checkpoint_df = checkpoint_df[[

        "calendar_date",
        "route_id",
        "checkpoint_name",
        "throughput_count",
        "congestion_level"
    ]]

    # ============================================
    # SELECT REQUIRED CROWD COLUMNS
    # ============================================

    crowd_df = crowd_df[[

        "calendar_date",
        "location_id",
        "pilgrim_count",
        "density_level",
        "avg_queue_minutes"
    ]]

    # ============================================
    # BASIC CLEANING
    # ============================================

    checkpoint_df.dropna(inplace=True)

    crowd_df.dropna(inplace=True)

    # ============================================
    # ALIGN DATASETS
    # ============================================

    min_rows = min(
        len(checkpoint_df),
        len(crowd_df)
    )

    checkpoint_df = checkpoint_df.head(
        min_rows
    ).copy()

    crowd_df = crowd_df.head(
        min_rows
    ).copy()

    print(f"\nAligned rows: {min_rows}")

    # ============================================
    # MAP DENSITY LEVEL TO NUMERIC VALUE
    # ============================================

    density_mapping = {

        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Severe": 4
    }

    crowd_df["crowd_density"] = (

        crowd_df["density_level"]
        .astype(str)
        .str.title()
        .map(density_mapping)
    )

    # ============================================
    # CREATE FINAL TRAFFIC DATASET
    # ============================================

    traffic_df = pd.DataFrame({

        "calendar_date":
            checkpoint_df["calendar_date"],

        "route_id":
            checkpoint_df["route_id"],

        "checkpoint_name":
            checkpoint_df["checkpoint_name"],

        "vehicle_count":
            checkpoint_df["throughput_count"],

        "congestion_level":
            checkpoint_df["congestion_level"],

        "crowd_density":
            crowd_df["crowd_density"]
    })

    # ============================================
    # REMOVE INVALID DENSITY ROWS
    # ============================================

    traffic_df.dropna(
        subset=["crowd_density"],
        inplace=True
    )

    # ============================================
    # RESET INDEX
    # ============================================

    traffic_df.reset_index(
        drop=True,
        inplace=True
    )

    # ============================================
    # DEBUG FINAL DATASET
    # ============================================

    print("\nFinal Traffic Dataset Shape:")
    print(traffic_df.shape)

    print("\nFinal Traffic Dataset Columns:")
    print(traffic_df.columns.tolist())

    print("\nFinal Traffic Dataset Sample:")
    print(traffic_df.head())

    return traffic_df