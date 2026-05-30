import pandas as pd

from datetime import datetime


class RiskForecaster:

    def __init__(self, state):

        self.state = state

        self.predictions = []

    # ========================================
    # OCCUPANCY RISK FORECAST
    # ========================================

    def forecast_occupancy_risk(self):

        risk_level = (
            self.state["risk_level"]
        )

        if risk_level == "high":

            prediction = {

                "forecast":
                    "traffic_surge",

                "probability":
                    0.85,

                "expected_impact":
                    "high congestion",

                "recommended_action":
                    "preemptive rerouting",

                "timestamp":
                    str(datetime.now())
            }

            self.predictions.append(
                prediction
            )

    # ========================================
    # CROWD PRESSURE FORECAST
    # ========================================

    def forecast_crowd_pressure(self):

        critical_domains = (

            self.state[
                "critical_domains"
            ]
        )

        if "crowd" in critical_domains:

            prediction = {

                "forecast":
                    "crowd_density_increase",

                "probability":
                    0.78,

                "expected_impact":
                    "queue escalation",

                "recommended_action":
                    "crowd redistribution",

                "timestamp":
                    str(datetime.now())
            }

            self.predictions.append(
                prediction
            )

    # ========================================
    # HEALTH LOAD FORECAST
    # ========================================

    def forecast_health_load(self):

        critical_domains = (

            self.state[
                "critical_domains"
            ]
        )

        if "health" in critical_domains:

            prediction = {

                "forecast":
                    "medical_pressure",

                "probability":
                    0.72,

                "expected_impact":
                    "medical queue increase",

                "recommended_action":
                    "increase emergency readiness",

                "timestamp":
                    str(datetime.now())
            }

            self.predictions.append(
                prediction
            )

    # ========================================
    # RUN FORECASTER
    # ========================================

    def run(self):

        self.forecast_occupancy_risk()

        self.forecast_crowd_pressure()

        self.forecast_health_load()

        print("\nRisk forecasting complete ✅")

        return self.predictions