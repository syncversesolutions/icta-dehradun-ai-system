class SemanticMemory:

    def __init__(self):

        self.knowledge_base = {

            "traffic_surge":

                "High occupancy increases congestion risk",

            "crowd_pressure":

                "Crowd buildup increases medical risk",

            "medical_pressure":

                "High density impacts emergency response"
        }

    # ========================================
    # GET KNOWLEDGE
    # ========================================

    def retrieve_knowledge(

        self,
        topic

    ):

        return self.knowledge_base.get(

            topic,

            "No knowledge available"
        )

    # ========================================
    # UPDATE KNOWLEDGE
    # ========================================

    def update_knowledge(

        self,
        topic,
        knowledge

    ):

        self.knowledge_base[
            topic
        ] = knowledge

        print(
            "\nSemantic knowledge updated ✅"
        )