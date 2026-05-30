class LearningEngine:

    def __init__(self):

        self.learning_history = []

    # ========================================
    # LEARN FROM FEEDBACK
    # ========================================

    def learn(

        self,
        feedback

    ):

        effectiveness = feedback[
            "effectiveness"
        ]

        if effectiveness == "high":

            learning = (

                "Workflow considered effective"
            )

        else:

            learning = (

                "Workflow requires optimization"
            )

        result = {

            "feedback":
                feedback,

            "learning":
                learning
        }

        self.learning_history.append(
            result
        )

        print(
            "\nLearning cycle complete ✅"
        )

        return result