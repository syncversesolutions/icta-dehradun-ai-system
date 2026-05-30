class AccommodationKPIEngine:

    def __init__(self, df):

        self.df = df

    # ========================================
    # OCCUPANCY RATE
    # ========================================

    def calculate_occupancy_rate(self):

        self.df["occupancy_rate"] = (

            self.df["occupied_rooms"] /

            self.df["total_rooms"]
        )

    # ========================================
    # CAPACITY UTILIZATION
    # ========================================

    def calculate_capacity_utilization(self):

        self.df["capacity_utilization"] = (

            self.df["active_bookings"] /

            self.df["maximum_capacity"]
        )

    # ========================================
    # BOOKING VELOCITY
    # ========================================

    def calculate_booking_velocity(self):

        self.df["booking_velocity"] = (

            self.df["new_bookings"] /

            self.df["time_interval"]
        )

    # ========================================
    # CHECKIN FLOW
    # ========================================

    def calculate_checkin_flow(self):

        self.df["checkin_flow"] = (

            self.df["checkins"] /

            self.df["time_interval"]
        )

    # ========================================
    # RUN KPI ENGINEERING
    # ========================================

    def run(self):

        self.calculate_occupancy_rate()

        self.calculate_capacity_utilization()

        self.calculate_booking_velocity()

        self.calculate_checkin_flow()

        print("\nAccommodation KPI engineering complete ✅")

        return self.df