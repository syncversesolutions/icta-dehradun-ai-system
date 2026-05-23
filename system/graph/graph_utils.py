# ============================================
# IMPORTS
# ============================================

import json

# ============================================
# LOAD DEPENDENCY GRAPH
# ============================================

def load_graph(graph_path):

    with open(
        graph_path,
        "r"
    ) as file:

        graph = json.load(file)

    return graph

# ============================================
# GET DOWNSTREAM IMPACTS
# ============================================

def get_downstream_impacts(

    graph,
    domain,
    metric
):

    try:

        impacts = (

            graph[domain]
            [metric]
            ["affects"]
        )

        return impacts

    except KeyError:

        return []

# ============================================
# GENERATE IMPACT ANALYSIS
# ============================================

def analyze_signal_impacts(

    graph,
    signal
):

    impacts = []

    domain = signal.get(
        "domain"
    )

    signal_type = signal.get(
        "signal_type"
    )

    # ============================================
    # TRAFFIC SIGNAL RULES
    # ============================================

    if domain == "traffic":

        downstream = get_downstream_impacts(

            graph,
            "traffic",
            "predicted_risk_level"
        )

        impacts.extend(
            downstream
        )

    return {

        "signal": signal,

        "downstream_impacts":
            impacts
    }