from datetime import datetime


class AlertEngine:

    def __init__(self):

        self.alerts = []

    # ========================================
    # ALERT SEVERITY
    # ========================================

    def determine_severity(

        self,
        risk_level,
        impact_count

    ):

        if (

            risk_level == "critical" or
            impact_count >= 10
        ):

            return "SEVERE"

        elif (

            risk_level == "high" or
            impact_count >= 5
        ):

            return "HIGH"

        elif (

            risk_level == "medium" or
            impact_count >= 2
        ):

            return "MODERATE"

        else:

            return "LOW"

    # ========================================
    # ACTION RECOMMENDATIONS
    # ========================================

    def generate_recommendations(

        self,
        affected_domains

    ):

        recommendations = []

        # ------------------------------------
        # TRAFFIC
        # ------------------------------------

        if "traffic" in affected_domains:

            recommendations.append(

                "Activate traffic rerouting"
            )

        # ------------------------------------
        # CROWD
        # ------------------------------------

        if "crowd" in affected_domains:

            recommendations.append(

                "Enable crowd redistribution"
            )

        # ------------------------------------
        # HEALTH
        # ------------------------------------

        if "health" in affected_domains:

            recommendations.append(

                "Increase medical readiness"
            )

        # ------------------------------------
        # GOVERNANCE
        # ------------------------------------

        if "governance" in affected_domains:

            recommendations.append(

                "Escalate governance coordination"
            )

        # ------------------------------------
        # ACCOMMODATION
        # ------------------------------------

        if "accommodation" in affected_domains:

            recommendations.append(

                "Monitor accommodation saturation"
            )

        # ------------------------------------
        # SYSTEM
        # ------------------------------------

        if "system" in affected_domains:

            recommendations.append(

                "Raise platform alert level"
            )

        return recommendations

    # ========================================
    # BUILD ALERT
    # ========================================

    def generate_alert(

        self,
        impact_analysis

    ):

        severity = (

            self.determine_severity(

                impact_analysis["risk_level"],
                impact_analysis["total_impacts"]
            )
        )

        recommendations = (

            self.generate_recommendations(

                impact_analysis[
                    "affected_domains"
                ]
            )
        )

        alert = {

            "source_signal":

                impact_analysis[
                    "source_signal"
                ],

            "risk_level":

                impact_analysis[
                    "risk_level"
                ],

            "severity":

                severity,

            "affected_domains":

                impact_analysis[
                    "affected_domains"
                ],

            "total_impacts":

                impact_analysis[
                    "total_impacts"
                ],

            "recommended_actions":

                recommendations,

            "timestamp":

                str(datetime.now())
        }

        self.alerts.append(alert)

        return alert

    # ========================================
    # DISPLAY ALERT
    # ========================================

    def display_alert(self, alert):

        print("\n")
        print("=" * 60)

        print("ICTA ALERT REPORT")

        print("=" * 60)

        print("\nSource Signal:")
        print(alert["source_signal"])

        print("\nRisk Level:")
        print(alert["risk_level"])

        print("\nSeverity:")
        print(alert["severity"])

        print("\nAffected Domains:")

        for domain in alert[
            "affected_domains"
        ]:

            print(f"   ↳ {domain}")

        print("\nRecommended Actions:")

        for action in alert[
            "recommended_actions"
        ]:

            print(f"   ✓ {action}")

        print("\nTotal Impacts:")
        print(alert["total_impacts"])

        print("\nTimestamp:")
        print(alert["timestamp"])

        print("\n")
        print("=" * 60)