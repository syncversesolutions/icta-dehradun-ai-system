class PolicyEngine:

    def __init__(self):

        self.policies = {

            "high_risk":

                "Escalate orchestration",

            "critical_risk":

                "Activate emergency mode",

            "crowd_pressure":

                "Enable redistribution",

            "traffic_pressure":

                "Trigger rerouting"
        }

    # ========================================
    # APPLY POLICIES
    # ========================================

    def apply_policies(

        self,
        risk_level,
        affected_domains

    ):

        actions = []

        # ------------------------------------
        # RISK POLICIES
        # ------------------------------------

        if risk_level == "high":

            actions.append(

                self.policies[
                    "high_risk"
                ]
            )

        if risk_level == "critical":

            actions.append(

                self.policies[
                    "critical_risk"
                ]
            )

        # ------------------------------------
        # DOMAIN POLICIES
        # ------------------------------------

        if "crowd" in affected_domains:

            actions.append(

                self.policies[
                    "crowd_pressure"
                ]
            )

        if "traffic" in affected_domains:

            actions.append(

                self.policies[
                    "traffic_pressure"
                ]
            )

        return actions