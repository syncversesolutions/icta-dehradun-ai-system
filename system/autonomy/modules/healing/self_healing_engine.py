from datetime import datetime


class SelfHealingEngine:

    def __init__(self):

        self.healing_log = []

    # ========================================
    # DETECT FAILURE
    # ========================================

    def detect_failure(

        self,
        workflow

    ):

        status = workflow.get(
            "status",
            "unknown"
        )

        if status != "completed":

            return True

        return False

    # ========================================
    # APPLY RECOVERY
    # ========================================

    def apply_recovery(

        self,
        workflow_name

    ):

        recovery = {

            "workflow":
                workflow_name,

            "recovery":
                "restart_execution",

            "timestamp":
                str(datetime.now())
        }

        self.healing_log.append(
            recovery
        )

        print(
            "\nSelf-healing recovery applied ✅"
        )

        return recovery