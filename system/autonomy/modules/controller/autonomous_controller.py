from system.autonomy.modules.workflow.workflow_engine import (
    WorkflowEngine
)

from system.autonomy.modules.executor.adaptive_executor import (
    AdaptiveExecutor
)


class AutonomousController:

    def __init__(self):

        self.workflow_engine = (
            WorkflowEngine()
        )

        self.executor = (
            AdaptiveExecutor()
        )

    # ========================================
    # RUN AUTONOMOUS FLOW
    # ========================================

    def run(

        self,
        execution_plan

    ):

        workflow = (

            self.workflow_engine
            .create_workflow(

                workflow_name=
                    "adaptive_response",

                actions=
                    execution_plan[
                        "actions"
                    ]
            )
        )

        executed = (

            self.workflow_engine
            .execute_workflow(
                workflow
            )
        )

        logs = (

            self.executor.execute(
                executed
            )
        )

        return {

            "workflow":
                executed,

            "execution_logs":
                logs
        }