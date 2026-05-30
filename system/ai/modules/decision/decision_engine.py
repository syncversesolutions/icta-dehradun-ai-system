from system.ai.policy.policy_engine import (
    PolicyEngine
)

from system.ai.recommendation.recommendation_engine import (
    RecommendationEngine
)

from system.ai.reasoning.reasoning_engine import (
    ReasoningEngine
)


class DecisionEngine:

    def __init__(self):

        self.policy_engine = (
            PolicyEngine()
        )

        self.recommendation_engine = (
            RecommendationEngine()
        )

        self.reasoning_engine = (
            ReasoningEngine()
        )

    # ========================================
    # RUN DECISION INTELLIGENCE
    # ========================================

    def run(

        self,
        state,
        predictions,
        trends

    ):

        affected_domains = (

            state[
                "critical_domains"
            ]
        )

        risk_level = (
            state["risk_level"]
        )

        # ------------------------------------
        # POLICY ACTIONS
        # ------------------------------------

        policy_actions = (

            self.policy_engine
            .apply_policies(

                risk_level,
                affected_domains
            )
        )

        # ------------------------------------
        # RECOMMENDATIONS
        # ------------------------------------

        recommendations = (

            self.recommendation_engine
            .run(
                affected_domains
            )
        )

        # ------------------------------------
        # REASONING
        # ------------------------------------

        reasoning = (

            self.reasoning_engine
            .reason(

                state,
                predictions,
                trends
            )
        )

        decision_output = {

            "policy_actions":
                policy_actions,

            "recommendations":
                recommendations,

            "reasoning":
                reasoning
        }

        print(
            "\nDecision intelligence complete ✅"
        )

        return decision_output