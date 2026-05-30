import json

from pathlib import Path

from datetime import datetime

from config.paths import BASE_DIR


class StateManager:

    def __init__(self):

        # ====================================
        # STATE FILE
        # ====================================

        self.state_path = (

            Path(BASE_DIR) /

            "system/state/system_state.json"
        )

        # ====================================
        # INITIALIZE STATE
        # ====================================

        self.initialize_state()

    # ========================================
    # INITIALIZE SYSTEM STATE
    # ========================================

    def initialize_state(self):

        if not self.state_path.exists():

            default_state = {

                "system_status":
                    "normal",

                "active_alerts":
                    [],

                "critical_domains":
                    [],

                "last_signal":
                    None,

                "last_orchestration":
                    None,

                "risk_level":
                    "low",

                "event_history_count":
                    0,

                "updated_at":
                    str(datetime.now())
            }

            with open(
                self.state_path,
                "w"
            ) as f:

                json.dump(
                    default_state,
                    f,
                    indent=4
                )

            print(
                "\nSystem state initialized ✅"
            )

    # ========================================
    # LOAD STATE
    # ========================================

    def load_state(self):

        with open(
            self.state_path,
            "r"
        ) as f:

            state = json.load(f)

        return state

    # ========================================
    # SAVE STATE
    # ========================================

    def save_state(self, state):

        state["updated_at"] = (
            str(datetime.now())
        )

        with open(
            self.state_path,
            "w"
        ) as f:

            json.dump(
                state,
                f,
                indent=4
            )

        print("\nSystem state updated ✅")

    # ========================================
    # UPDATE FROM ALERT
    # ========================================

    def update_from_alert(

        self,
        alert

    ):

        state = self.load_state()

        state["system_status"] = (

            "critical"

            if alert["severity"] == "SEVERE"

            else "elevated"
        )

        state["risk_level"] = (
            alert["risk_level"]
        )

        state["active_alerts"].append({

            "source_signal":
                alert["source_signal"],

            "severity":
                alert["severity"],

            "timestamp":
                alert["timestamp"]
        })

        state["critical_domains"] = (

            alert["affected_domains"]
        )

        state["last_signal"] = (
            alert["source_signal"]
        )

        state["last_orchestration"] = (
            str(datetime.now())
        )

        state["event_history_count"] += 1

        self.save_state(state)

        return state

    # ========================================
    # DISPLAY STATE
    # ========================================

    def display_state(self):

        state = self.load_state()

        print("\n")
        print("=" * 60)

        print("ICTA SYSTEM STATE")

        print("=" * 60)

        print("\nSystem Status:")
        print(state["system_status"])

        print("\nRisk Level:")
        print(state["risk_level"])

        print("\nCritical Domains:")

        for domain in state[
            "critical_domains"
        ]:

            print(f"   ↳ {domain}")

        print("\nActive Alerts:")

        for alert in state[
            "active_alerts"
        ]:

            print(
                f"   ✓ "
                f"{alert['source_signal']} "
                f"({alert['severity']})"
            )

        print("\nEvent History Count:")
        print(
            state["event_history_count"]
        )

        print("\nLast Signal:")
        print(state["last_signal"])

        print("\nUpdated At:")
        print(state["updated_at"])

        print("\n")
        print("=" * 60)