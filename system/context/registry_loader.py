import json
from pathlib import Path

from config.paths import BASE_DIR


class RegistryLoader:

    def __init__(self):

        self.architecture_path = Path(BASE_DIR) / "architecture"
        self.system_path = Path(BASE_DIR) / "system"

    # =====================================
    # DOMAIN REGISTRY
    # =====================================

    def load_domains(self):

        file_path = (
            self.architecture_path /
            "domain_registry.json"
        )

        with open(file_path, "r") as f:
            return json.load(f)

    # =====================================
    # KPI REGISTRY
    # =====================================

    def load_kpis(self):

        file_path = (
            self.architecture_path /
            "kpi_registry.json"
        )

        with open(file_path, "r") as f:
            return json.load(f)

    # =====================================
    # SIGNAL REGISTRY
    # =====================================

    def load_signals(self):

        file_path = (
            self.architecture_path /
            "signal_registry.json"
        )

        with open(file_path, "r") as f:
            return json.load(f)

    # =====================================
    # DEPENDENCY GRAPH
    # =====================================

    def load_dependency_graph(self):

        file_path = (
            Path(BASE_DIR) /
            "system" /
            "graph" /
            "dependency_graph.json"
        )

        with open(file_path, "r") as f:
            return json.load(f)

    # =====================================
    # PIPELINE REGISTRY
    # =====================================

    def load_pipeline_registry(self):

        file_path = (
            Path(BASE_DIR) /
            "system" /
            "orchestration" /
            "pipeline_registry.json"
        )

        with open(file_path, "r") as f:
            return json.load(f)