import json

from pathlib import Path

from config.paths import BASE_DIR

from system.orchestration.modules.coordination.orchestration_manager import (
    OrchestrationManager
)


class SignalRouter:

    def __init__(self):

        # ====================================
        # ORCHESTRATION MANAGER
        # ====================================

        self.manager = (
            OrchestrationManager()
        )

        # ====================================
        # ROUTING HISTORY
        # ====================================

        self.routing_history = []

    # ========================================
    # LOAD SIGNAL FILE
    # ========================================

    def load_signals(

        self,
        signal_path

    ):

        with open(signal_path, "r") as f:

            signals = json.load(f)

        print("\nSignals loaded ✅")

        return signals

    # ========================================
    # FILTER CRITICAL SIGNALS
    # ========================================

    def filter_critical_signals(

        self,
        signals

    ):

        critical_signals = []

        for signal in signals:

            status = signal.get(
                "status",
                "normal"
            )

            if status == "critical":

                critical_signals.append(
                    signal
                )

        print(
            f"\nCritical signals detected: "
            f"{len(critical_signals)}"
        )

        return critical_signals

    # ========================================
    # BUILD SIGNAL NODE
    # ========================================

    def build_signal_node(

        self,
        signal

    ):

        domain = signal.get(
            "domain",
            "unknown"
        )

        signal_name = signal.get(
            "signal",
            "unknown"
        )

        # ------------------------------------
        # SIGNAL → GRAPH NODE MAPPING
        # ------------------------------------

        mapping = {

            "high_occupancy":
                "accommodation.occupancy_rate",

            "overcapacity_risk":
                "accommodation.capacity_utilization",

            "booking_surge":
                "accommodation.booking_velocity",

            "high_checkin_flow":
                "accommodation.checkin_flow"
        }

        node = mapping.get(

            signal_name,

            f"{domain}.{signal_name}"
        )

        return node

    # ========================================
    # ROUTE SIGNAL
    # ========================================

    def route_signal(

        self,
        signal

    ):

        signal_node = (

            self.build_signal_node(
                signal
            )
        )

        print("\nRouting Signal:")
        print(signal_node)

        result = (

            self.manager.orchestrate(
                signal_node
            )
        )

        self.routing_history.append({

            "signal":
                signal,

            "signal_node":
                signal_node,

            "result":
                result
        })

    # ========================================
    # ROUTE ALL SIGNALS
    # ========================================

    def route_signals(

        self,
        signal_path

    ):

        signals = (

            self.load_signals(
                signal_path
            )
        )

        critical_signals = (

            self.filter_critical_signals(
                signals
            )
        )

        if len(critical_signals) == 0:

            print("\nNo critical signals detected ✅")

            return

        for signal in critical_signals:

            self.route_signal(signal)

        print("\n")
        print("=" * 60)

        print("SIGNAL ROUTING COMPLETE")

        print("=" * 60)