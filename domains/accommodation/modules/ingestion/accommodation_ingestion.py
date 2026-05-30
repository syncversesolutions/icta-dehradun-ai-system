import pandas as pd


class AccommodationIngestion:

    def __init__(self):

        self.booking_df = None

        self.occupancy_df = None

        self.checkin_df = None

    # ========================================
    # LOAD BOOKING LOGS
    # ========================================

    def load_booking_logs(self, path):

        self.booking_df = pd.read_csv(path)

        print("\nBooking logs loaded ✅")

    # ========================================
    # LOAD OCCUPANCY LOGS
    # ========================================

    def load_occupancy_logs(self, path):

        self.occupancy_df = pd.read_csv(path)

        print("\nOccupancy logs loaded ✅")

    # ========================================
    # LOAD CHECKIN LOGS
    # ========================================

    def load_checkin_logs(self, path):

        self.checkin_df = pd.read_csv(path)

        print("\nCheckin logs loaded ✅")

    # ========================================
    # CLEAN DATAFRAME
    # ========================================

    def clean_dataframe(self, df):

        df.columns = (

            df.columns
            .str.strip()
            .str.lower()
        )

        df.drop_duplicates(inplace=True)

        return df

    # ========================================
    # BUILD DATASET
    # ========================================

    def build_dataset(self):

        booking_df = self.clean_dataframe(
            self.booking_df
        )

        occupancy_df = self.clean_dataframe(
            self.occupancy_df
        )

        checkin_df = self.clean_dataframe(
            self.checkin_df
        )

        min_rows = min(

            len(booking_df),
            len(occupancy_df),
            len(checkin_df)
        )

        booking_df = booking_df.head(min_rows)

        occupancy_df = occupancy_df.head(min_rows)

        checkin_df = checkin_df.head(min_rows)

        df = pd.DataFrame()

        df["occupied_rooms"] = (
            occupancy_df.get(
                "occupied_rooms",
                0
            )
        )

        df["total_rooms"] = (
            occupancy_df.get(
                "total_rooms",
                1
            )
        )

        df["active_bookings"] = (
            booking_df.get(
                "active_bookings",
                0
            )
        )

        df["maximum_capacity"] = (
            occupancy_df.get(
                "maximum_capacity",
                df["total_rooms"]
            )
        )

        df["new_bookings"] = (
            booking_df.get(
                "new_bookings",
                0
            )
        )

        df["checkins"] = (
            checkin_df.get(
                "checkins",
                0
            )
        )

        df["time_interval"] = 1

        print("\nAccommodation dataset built ✅")

        return df