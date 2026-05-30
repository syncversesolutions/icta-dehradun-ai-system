from datetime import datetime


class RecommendationEngine:

    def __init__(self):

        self.recommendations = []

    # ========================================
    # TRAFFIC RECOMMENDATION
    # ========================================

    def traffic_recommendation(

        self,
        affected_domains

    ):

        if "traffic" in affected_domains:

            recommendation = {

                "domain":
                    "traffic",

                "recommendation":

                    "Activate dynamic rerouting",

                "priority":
                    "high",

                "timestamp":
                    str(datetime.now())
            }

            self.recommendations.append(
                recommendation
            )

    # ========================================
    # CROWD RECOMMENDATION
    # ========================================

    def crowd_recommendation(

        self,
        affected_domains

    ):

        if "crowd" in affected_domains:

            recommendation = {

                "domain":
                    "crowd",

                "recommendation":

                    "Enable crowd redistribution",

                "priority":
                    "high",

                "timestamp":
                    str(datetime.now())
            }

            self.recommendations.append(
                recommendation
            )

    # ========================================
    # HEALTH RECOMMENDATION
    # ========================================

    def health_recommendation(

        self,
        affected_domains

    ):

        if "health" in affected_domains:

            recommendation = {

                "domain":
                    "health",

                "recommendation":

                    "Increase emergency medical readiness",

                "priority":
                    "medium",

                "timestamp":
                    str(datetime.now())
            }

            self.recommendations.append(
                recommendation
            )

    # ========================================
    # RUN ENGINE
    # ========================================

    def run(

        self,
        affected_domains

    ):

        self.traffic_recommendation(
            affected_domains
        )

        self.crowd_recommendation(
            affected_domains
        )

        self.health_recommendation(
            affected_domains
        )

        print(
            "\nRecommendations generated ✅"
        )

        return self.recommendations