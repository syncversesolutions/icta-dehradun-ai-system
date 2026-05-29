from pathlib import Path

from config.paths import BASE_DIR
from system.context.registry_loader import RegistryLoader


class ArchitectureReport:

    def __init__(self):

        self.loader = RegistryLoader()

        self.root = Path(BASE_DIR)

    # =========================================
    # DOMAIN REPORT
    # =========================================

    def domain_report(self):

        registry = self.loader.load_domains()

        print("\n")
        print("=" * 50)
        print("DOMAIN STATUS")
        print("=" * 50)

        for domain, config in registry.items():

            status = config.get(
                "status",
                "unknown"
            )

            visible = config.get(
                "show_on_dashboard",
                False
            )

            print(f"\nDomain: {domain}")
            print(f"Status: {status}")
            print(f"Dashboard Visible: {visible}")

    # =========================================
    # KPI REPORT
    # =========================================

    def kpi_report(self):

        kpis = self.loader.load_kpis()

        print("\n")
        print("=" * 50)
        print("KPI STATUS")
        print("=" * 50)

        total = 0

        for domain, items in kpis.items():

            count = len(items)

            total += count

            print(
                f"{domain}: {count} KPIs"
            )

        print(f"\nTotal KPIs: {total}")

    # =========================================
    # SIGNAL REPORT
    # =========================================

    def signal_report(self):

        signals = self.loader.load_signals()

        print("\n")
        print("=" * 50)
        print("SIGNAL STATUS")
        print("=" * 50)

        total = 0

        for domain, items in signals.items():

            count = len(items)

            total += count

            print(
                f"{domain}: {count} signals"
            )

        print(f"\nTotal Signals: {total}")

   # =========================================
    # DEPENDENCY REPORT
    # =========================================

    def dependency_report(self):

        graph = self.loader.load_dependency_graph()

        print("\n")
        print("=" * 50)
        print("DEPENDENCY GRAPH")
        print("=" * 50)

        total_nodes = len(graph)

        total_edges = 0

        for node, config in graph.items():

            affects = config.get(
                "affects",
                []
            )

            edge_count = len(affects)

            total_edges += edge_count

            print(
                f"{node} -> {edge_count} dependencies"
            )

            for target in affects:

                print(f"   ↳ {target}")

        print(f"\nNodes: {total_nodes}")
        print(f"Edges: {total_edges}")

    # =========================================
    # PIPELINE REPORT
    # =========================================

    def pipeline_report(self):

        pipelines = (
            self.loader
            .load_pipeline_registry()
        )

        print("\n")
        print("=" * 50)
        print("PIPELINE STATUS")
        print("=" * 50)

        for domain, items in pipelines.items():

            print(
                f"{domain}: "
                f"{len(items)} pipelines"
            )

    # =========================================
    # FULL REPORT
    # =========================================

    def run(self):

        print("\n")
        print("=" * 60)
        print("ICTA ARCHITECTURE REPORT")
        print("=" * 60)

        self.domain_report()

        self.kpi_report()

        self.signal_report()

        self.dependency_report()

        self.pipeline_report()

        print("\n")
        print("=" * 60)
        print("ARCHITECTURE REPORT COMPLETE")
        print("=" * 60)