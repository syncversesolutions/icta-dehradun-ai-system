class FeedbackEngine:

    def __init__(self):

        self.feedback_log = []

    # ========================================
    # CAPTURE FEEDBACK
    # ========================================

    def capture_feedback(

        self,
        workflow_name,
        effectiveness

    ):

        feedback = {

            "workflow":
                workflow_name,

            "effectiveness":
                effectiveness
        }

        self.feedback_log.append(
            feedback
        )

        print(
            "\nOperational feedback captured ✅"
        )

        return feedback