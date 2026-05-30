from datetime import datetime


class AccommodationSignalEngine:

    def __init__(self, df):

        self.df = df

        self.signals = []

    # ========================================
    # HIGH OCCUPANCY SIGNAL
    # ========================================

    def high_occupancy_signal(self):

        avg_occupancy = (

            self.df["occupancy_rate"]
            .mean()
        )

        signal = {

            "domain":
                "accommodation",

            "signal":
                "high_occupancy",

            "value":
                float(avg_occupancy),

            "threshold":
                0.85,

            "status":
                "critical"
                if avg_occupancy > 0.85
                else "normal",

            "timestamp":
                str(datetime.now())
        }

        self.signals.append(signal)

    # ========================================
    # OVERCAPACITY RISK SIGNAL
    # ========================================

    def overcapacity_risk_signal(self):

        avg_utilization = (

            self.df["capacity_utilization"]
            .mean()
        )

        signal = {

            "domain":
                "accommodation",

            "signal":
                "overcapacity_risk",

            "value":
                float(avg_utilization),

            "threshold":
                0.90,

            "status":
                "critical"
                if avg_utilization > 0.90
                else "normal",

            "timestamp":
                str(datetime.now())
        }

        self.signals.append(signal)

    # ========================================
    # BOOKING SURGE SIGNAL
    # ========================================

    def booking_surge_signal(self):

        avg_velocity = (

            self.df["booking_velocity"]
            .mean()
        )

        signal = {

            "domain":
                "accommodation",

            "signal":
                "booking_surge",

            "value":
                float(avg_velocity),

            "threshold":
                50,

            "status":
                "critical"
                if avg_velocity > 50
                else "normal",

            "timestamp":
                str(datetime.now())
        }

        self.signals.append(signal)

    # ========================================
    # CHECKIN FLOW SIGNAL
    # ========================================

    def high_checkin_flow_signal(self):

        avg_checkin_flow = (

            self.df["checkin_flow"]
            .mean()
        )

        signal = {

            "domain":
                "accommodation",

            "signal":
                "high_checkin_flow",

            "value":
                float(avg_checkin_flow),

            "threshold":
                40,

            "status":
                "critical"
                if avg_checkin_flow > 40
                else "normal",

            "timestamp":
                str(datetime.now())
        }

        self.signals.append(signal)

    # ========================================
    # RUN SIGNAL ENGINE
    # ========================================

    def run(self):

        self.high_occupancy_signal()

        self.overcapacity_risk_signal()

        self.booking_surge_signal()

        self.high_checkin_flow_signal()

        print("\nAccommodation signals generated ✅")

        return self.signals