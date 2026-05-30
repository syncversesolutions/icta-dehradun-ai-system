class OntologyEngine:

    def __init__(self):

        self.ontology = {

            "traffic":

                "Mobility and congestion domain",

            "crowd":

                "Pilgrim density and movement domain",

            "health":

                "Medical and emergency response domain",

            "accommodation":

                "Occupancy and lodging domain"
        }

    # ========================================
    # GET DOMAIN DEFINITION
    # ========================================

    def get_definition(

        self,
        domain

    ):

        return self.ontology.get(

            domain,

            "No ontology available"
        )

    # ========================================
    # UPDATE ONTOLOGY
    # ========================================

    def update_ontology(

        self,
        domain,
        definition

    ):

        self.ontology[
            domain
        ] = definition

        print(
            "\nOntology updated ✅"
        )