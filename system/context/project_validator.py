from pathlib import Path

from config.paths import BASE_DIR
from system.context.registry_loader import RegistryLoader


class ProjectValidator:

    def __init__(self):

        self.loader = RegistryLoader()

        self.root = Path(BASE_DIR)

        self.results = []

    # ====================================
    # CHECK FILE
    # ====================================

    def check_exists(self, path, label):

        if Path(path).exists():

            self.results.append(
                f"✅ {label}"
            )

            return True

        self.results.append(
            f"❌ {label}"
        )

        return False

    # ====================================
    # REGISTRY CHECKS
    # ====================================

    def validate_registries(self):

        self.check_exists(
            self.root /
            "architecture" /
            "domain_registry.json",
            "Domain Registry"
        )

        self.check_exists(
            self.root /
            "architecture" /
            "kpi_registry.json",
            "KPI Registry"
        )

        self.check_exists(
            self.root /
            "architecture" /
            "signal_registry.json",
            "Signal Registry"
        )

    # ====================================
    # SYSTEM CHECKS
    # ====================================

    def validate_system(self):

        self.check_exists(
            self.root /
            "system" /
            "graph" /
            "dependency_graph.json",
            "Dependency Graph"
        )

        self.check_exists(
            self.root /
            "system" /
            "orchestration" /
            "pipeline_registry.json",
            "Pipeline Registry"
        )

    # ====================================
    # DOMAIN CHECKS
    # ====================================

    def validate_domains(self):

        registry = self.loader.load_domains()

        for domain_name in registry.keys():

            domain_path = (
                self.root /
                "domains" /
                domain_name
            )

            self.check_exists(
                domain_path,
                f"Domain: {domain_name}"
            )

    # ====================================
    # RUN
    # ====================================

    def run(self):

        print("\n")
        print("=" * 50)
        print("ICTA PROJECT VALIDATOR")
        print("=" * 50)

        self.validate_registries()

        self.validate_system()

        self.validate_domains()

        print("\n")

        for result in self.results:

            print(result)

        print("\n")
        print("=" * 50)