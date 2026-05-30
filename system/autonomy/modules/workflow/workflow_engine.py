from datetime import datetime


class WorkflowEngine:

    def __init__(self):

        self.active_workflows = []

    # ========================================
    # CREATE WORKFLOW
    # ========================================

    def create_workflow(

        self,
        workflow_name,
        actions

    ):

        workflow = {

            "workflow":
                workflow_name,

            "actions":
                actions,

            "status":
                "initialized",

            "timestamp":
                str(datetime.now())
        }

        self.active_workflows.append(
            workflow
        )

        print(
            "\nWorkflow created ✅"
        )

        return workflow

    # ========================================
    # EXECUTE WORKFLOW
    # ========================================

    def execute_workflow(

        self,
        workflow

    ):

        print("\n")
        print("=" * 60)

        print(
            f"EXECUTING: "
            f"{workflow['workflow']}"
        )

        print("=" * 60)

        for action in workflow[
            "actions"
        ]:

            print(f"\n✓ {action}")

        workflow["status"] = (
            "completed"
        )

        workflow[
            "completed_at"
        ] = str(datetime.now())

        print("\nWorkflow execution complete ✅")

        return workflow