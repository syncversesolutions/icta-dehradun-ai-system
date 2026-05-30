import json

from pathlib import Path

from config.paths import BASE_DIR


class ImpactEngine:

    def __init__(self):

        self.graph = self.load_graph()

    # ========================================
    # LOAD DEPENDENCY GRAPH
    # ========================================

    def load_graph(self):

        graph_path = (

            Path(BASE_DIR) /

            "system/graph/dependency_graph.json"
        )

        with open(graph_path, "r") as f:

            graph = json.load(f)

        print("\nDependency graph loaded ✅")

        return graph

    # ========================================
    # GET DIRECT IMPACTS
    # ========================================

    def get_direct_impacts(self, node):

        if node not in self.graph:

            return []

        impacts = (

            self.graph[node]
            .get("affects", [])
        )

        return impacts

    # ========================================
    # RECURSIVE IMPACT PROPAGATION
    # ========================================

    def propagate_impacts(

        self,
        node,
        visited=None

    ):

        if visited is None:

            visited = set()

        if node in visited:

            return []

        visited.add(node)

        downstream = []

        direct_impacts = (

            self.get_direct_impacts(node)
        )

        for impact in direct_impacts:

            downstream.append(impact)

            child_impacts = (

                self.propagate_impacts(
                    impact,
                    visited
                )
            )

            downstream.extend(child_impacts)

        return list(set(downstream))

    # ========================================
    # DOMAIN EXTRACTION
    # ========================================

    def extract_domains(self, impacts):

        domains = set()

        for impact in impacts:

            domain = impact.split(".")[0]

            domains.add(domain)

        return list(domains)

    # ========================================
    # RISK SCORING
    # ========================================

    def calculate_risk_level(

        self,
        impact_count

    ):

        if impact_count >= 10:

            return "critical"

        elif impact_count >= 5:

            return "high"

        elif impact_count >= 2:

            return "medium"

        else:

            return "low"

    # ========================================
    # IMPACT ANALYSIS
    # ========================================

    def analyze_signal(

        self,
        signal_node

    ):

        impacts = (

            self.propagate_impacts(
                signal_node
            )
        )

        affected_domains = (

            self.extract_domains(
                impacts
            )
        )

        risk_level = (

            self.calculate_risk_level(
                len(impacts)
            )
        )

        result = {

            "source_signal":
                signal_node,

            "affected_nodes":
                impacts,

            "affected_domains":
                affected_domains,

            "total_impacts":
                len(impacts),

            "risk_level":
                risk_level
        }

        return result

    # ========================================
    # DISPLAY ANALYSIS
    # ========================================

    def display_analysis(

        self,
        analysis

    ):

        print("\n")
        print("=" * 60)

        print("IMPACT ANALYSIS REPORT")

        print("=" * 60)

        print("\nSource Signal:")
        print(
            analysis["source_signal"]
        )

        print("\nAffected Domains:")
        print(
            analysis["affected_domains"]
        )

        print("\nRisk Level:")
        print(
            analysis["risk_level"]
        )

        print("\nAffected Nodes:")

        for node in analysis["affected_nodes"]:

            print(f"   ↳ {node}")

        print("\nTotal Impacts:")
        print(
            analysis["total_impacts"]
        )

        print("\n")
        print("=" * 60)