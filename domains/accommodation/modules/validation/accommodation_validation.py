import pandas as pd


class AccommodationValidation:

    def __init__(self):

        self.df = None

    # ========================================
    # LOAD DATASET
    # ========================================

    def load_dataset(self, path):

        self.df = pd.read_csv(path)

        print("\nAccommodation dataset loaded ✅")

        print("\nDataset Shape:")
        print(self.df.shape)

    # ========================================
    # REMOVE NULL VALUES
    # ========================================

    def remove_nulls(self):

        before = self.df.shape[0]

        self.df.dropna(inplace=True)

        after = self.df.shape[0]

        print("\nNull rows removed:")
        print(before - after)

    # ========================================
    # VALIDATE TOTAL ROOMS
    # ========================================

    def validate_total_rooms(self):

        self.df = self.df[
            self.df["total_rooms"] > 0
        ]

        print("\nTotal rooms validated ✅")

    # ========================================
    # VALIDATE MAX CAPACITY
    # ========================================

    def validate_capacity(self):

        self.df = self.df[
            self.df["maximum_capacity"] > 0
        ]

        print("\nMaximum capacity validated ✅")

    # ========================================
    # VALIDATE OCCUPIED ROOMS
    # ========================================

    def validate_occupied_rooms(self):

        self.df = self.df[
            self.df["occupied_rooms"] >= 0
        ]

        print("\nOccupied rooms validated ✅")

    # ========================================
    # VALIDATE BOOKINGS
    # ========================================

    def validate_bookings(self):

        self.df = self.df[
            self.df["active_bookings"] >= 0
        ]

        print("\nBookings validated ✅")

    # ========================================
    # RUN FULL VALIDATION
    # ========================================

    def run_validation(self):

        self.remove_nulls()

        self.validate_total_rooms()

        self.validate_capacity()

        self.validate_occupied_rooms()

        self.validate_bookings()

        print("\nValidation complete ✅")

        print("\nValidated Shape:")
        print(self.df.shape)

        return self.df