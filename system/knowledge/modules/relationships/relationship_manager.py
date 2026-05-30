class RelationshipManager:

    def __init__(self):

        self.relationships = []

    # ========================================
    # REGISTER RELATIONSHIP
    # ========================================

    def register(

        self,
        source,
        target,
        relationship

    ):

        relation = {

            "source":
                source,

            "target":
                target,

            "relationship":
                relationship
        }

        self.relationships.append(
            relation
        )

        print(
            "\nRelationship registered ✅"
        )

        return relation

    # ========================================
    # GET RELATIONSHIPS
    # ========================================

    def get_relationships(self):

        return self.relationships