import json

from datetime import datetime

from system.orchestration.impact_engine import (
    ImpactEngine
)

from system.orchestration.alert_engine import (
    AlertEngine
)

from system.state.state_manager import (
    StateManager
)


class OrchestrationManager:

    def __init__(self):

        # ====================================
        # ENGINES
        # ====================================

        self.impact_engine = (
            ImpactEngine()
        )

        self.alert_engine = (
            AlertEngine()
        )

        # ====================================
        # STATE MANAGER
        # ====================================

        self.state_manager = (
            StateManager()
        )

        # ====================================
        # ORCHESTRATION HISTORY
        # ====================================

        self.history = []

    # ========================================
    # RUN IMPACT ANALYSIS
    # ========================================

    def analyze_signal(

        self,
        signal_node

    ):

        analysis = (

            self.impact_engine
            .analyze_signal(signal_node)
        )

        return analysis

    # ========================================
    # GENERATE ALERT
    # ========================================

    def generate_alert(

        self,
        analysis

    ):

        alert = (

            self.alert_engine
            .generate_alert(analysis)
        )

        return alert

    # ========================================
    # EXECUTION DECISION
    # ========================================

    def determine_execution_plan(

        self,
        alert

    ):

        severity = (
            alert["severity"]
        )

        affected_domains = (
            alert["affected_domains"]
        )

        execution_plan = {

            "severity":
                severity,

            "actions":
                []
        }

        # ------------------------------------
        # SEVERE
        # ------------------------------------

        if severity == "SEVERE":

            execution_plan[
                "actions"
            ].append(

                "Activate emergency orchestration"
            )

            execution_plan[
                "actions"
            ].append(

                "Trigger all critical pipelines"
            )

        # ------------------------------------
        # HIGH
        # ------------------------------------

        elif severity == "HIGH":

            execution_plan[
                "actions"
            ].append(

                "Trigger affected domain pipelines"
            )

            execution_plan[
                "actions"
            ].append(

                "Increase monitoring frequency"
            )

        # ------------------------------------
        # MODERATE
        # ------------------------------------

        elif severity == "MODERATE":

            execution_plan[
                "actions"
            ].append(

                "Enable enhanced monitoring"
            )

        # ------------------------------------
        # LOW
        # ------------------------------------

        else:

            execution_plan[
                "actions"
            ].append(

                "Log event for observation"
            )

        # ------------------------------------
        # DOMAIN ACTIONS
        # ------------------------------------

        if "traffic" in affected_domains:

            execution_plan[
                "actions"
            ].append(

                "Run traffic prediction pipeline"
            )

        if "crowd" in affected_domains:

            execution_plan[
                "actions"
            ].append(

                "Run crowd density analysis"
            )

        if "health" in affected_domains:

            execution_plan[
                "actions"
            ].append(

                "Increase medical readiness checks"
            )

        if "accommodation" in affected_domains:

            execution_plan[
                "actions"
            ].append(

                "Run occupancy optimization"
            )

        return execution_plan

    # ========================================
    # STORE HISTORY
    # ========================================

    def store_event(

        self,
        signal_node,
        analysis,
        alert,
        execution_plan

    ):

        event = {

            "signal":
                signal_node,

            "analysis":
                analysis,

            "alert":
                alert,

            "execution_plan":
                execution_plan,

            "timestamp":
                str(datetime.now())
        }

        self.history.append(event)

    # ========================================
    # FULL ORCHESTRATION
    # ========================================

    def orchestrate(

        self,
        signal_node

    ):

        print("\n")
        print("=" * 60)

        print("ICTA ORCHESTRATION STARTED")

        print("=" * 60)

        # ------------------------------------
        # IMPACT ANALYSIS
        # ------------------------------------

        analysis = (
            self.analyze_signal(
                signal_node
            )
        )

        # ------------------------------------
        # ALERT GENERATION
        # ------------------------------------

        alert = (
            self.generate_alert(
                analysis
            )
        )

        # ------------------------------------
        # EXECUTION PLAN
        # ------------------------------------

        execution_plan = (

            self.determine_execution_plan(
                alert
            )
        )

        # ------------------------------------
        # STORE EVENT
        # ------------------------------------

        self.store_event(

            signal_node,
            analysis,
            alert,
            execution_plan
        )

        # ------------------------------------
        # UPDATE SYSTEM STATE
        # ------------------------------------

        self.state_manager.update_from_alert(
            alert
        )

        # ------------------------------------
        # DISPLAY RESULTS
        # ------------------------------------

        self.display_orchestration(

            analysis,
            alert,
            execution_plan
        )

        return {

            "analysis":
                analysis,

            "alert":
                alert,

            "execution_plan":
                execution_plan
        }

    # ========================================
    # DISPLAY ORCHESTRATION
    # ========================================

    def display_orchestration(

        self,
        analysis,
        alert,
        execution_plan

    ):

        print("\nSource Signal:")
        print(
            analysis["source_signal"]
        )

        print("\nRisk Level:")
        print(
            alert["risk_level"]
        )

        print("\nSeverity:")
        print(
            alert["severity"]
        )

        print("\nAffected Domains:")

        for domain in alert[
            "affected_domains"
        ]:

            print(f"   ↳ {domain}")

        print("\nExecution Plan:")

        for action in execution_plan[
            "actions"
        ]:

            print(f"   ✓ {action}")

        print("\n")
        print("=" * 60)

        print("ICTA ORCHESTRATION COMPLETE")

        print("=" * 60)