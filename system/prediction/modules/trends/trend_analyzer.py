import pandas as pd


class TrendAnalyzer:

    def __init__(self, df):

        self.df = df

    # ========================================
    # OCCUPANCY TREND
    # ========================================

    def occupancy_trend(self):

        trend = (

            self.df[
                "occupancy_rate"
            ].mean()
        )

        if trend > 0.85:

            return "rising"

        return "stable"

    # ========================================
    # BOOKING TREND
    # ========================================

    def booking_trend(self):

        trend = (

            self.df[
                "booking_velocity"
            ].mean()
        )

        if trend > 50:

            return "surging"

        return "normal"

    # ========================================
    # CHECKIN TREND
    # ========================================

    def checkin_trend(self):

        trend = (

            self.df[
                "checkin_flow"
            ].mean()
        )

        if trend > 40:

            return "heavy"

        return "moderate"

    # ========================================
    # ANALYZE ALL
    # ========================================

    def analyze(self):

        analysis = {

            "occupancy_trend":
                self.occupancy_trend(),

            "booking_trend":
                self.booking_trend(),

            "checkin_trend":
                self.checkin_trend()
        }

        print("\nTrend analysis complete ✅")

        return analysis