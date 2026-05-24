# ============================================
# GENERATE OPERATIONAL ALERTS
# ============================================

def generate_alerts(

    impact_analysis
):

    alerts = []

    for item in impact_analysis:

        signal = item["signal"]

        downstream_impacts = (

            item["downstream_impacts"]
        )

        risk_level = signal.get(
            "risk_level",
            "Low"
        )

        # ============================================
        # SEVERITY SCORING
        # ============================================

        severity_score = 0

        if risk_level == "Severe":

            severity_score = 4

        elif risk_level == "High":

            severity_score = 3

        elif risk_level == "Medium":

            severity_score = 2

        else:

            severity_score = 1

        # ============================================
        # ALERT PRIORITY
        # ============================================

        if severity_score >= 4:

            priority = "CRITICAL"

        elif severity_score >= 3:

            priority = "HIGH"

        elif severity_score >= 2:

            priority = "MEDIUM"

        else:

            priority = "LOW"

        # ============================================
        # CREATE ALERT OBJECT
        # ============================================

        alert = {

            "domain":
                signal.get("domain"),

            "signal_type":
                signal.get("signal_type"),

            "route_id":
                signal.get("route_id"),

            "checkpoint_name":
                signal.get(
                    "checkpoint_name"
                ),

            "risk_level":
                risk_level,

            "priority":
                priority,

            "severity_score":
                severity_score,

            "downstream_impacts":
                downstream_impacts,

            "recommended_action":
                signal.get(
                    "recommended_action"
                )
        }

        alerts.append(alert)

    return alerts