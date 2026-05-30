import networkx as nx


class GraphEngine:

    def __init__(self):

        self.graph = nx.DiGraph()

    # ========================================
    # ADD RELATIONSHIP
    # ========================================

    def add_relationship(

        self,
        source,
        target,
        relationship

    ):

        self.graph.add_edge(

            source,
            target,

            relationship=relationship
        )

        print(
            "\nRelationship added ✅"
        )

    # ========================================
    # GET CONNECTED NODES
    # ========================================

    def connected_nodes(

        self,
        node

    ):

        if node not in self.graph:

            return []

        return list(
            self.graph.successors(node)
        )

    # ========================================
    # DISPLAY GRAPH
    # ========================================

    def display_graph(self):

        print("\n")
        print("=" * 60)

        print("ICTA KNOWLEDGE GRAPH")

        print("=" * 60)

        for edge in self.graph.edges(data=True):

            source, target, data = edge

            print(
                f"\n{source} "
                f"→ {target} "
                f"({data['relationship']})"
            )

        print("\n")
        print("=" * 60)