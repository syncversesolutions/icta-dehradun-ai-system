import os

# ============================================
# PROJECT ROOT
# ============================================

BASE_DIR = "/content/drive/MyDrive/project_cd"

# ============================================
# PATH REGISTRY
# ============================================

PATHS = {

    # =====================================================
    # TRAFFIC DOMAIN
    # =====================================================

    "traffic": {

        # RAW DATA
        "raw":
            BASE_DIR +
            "/domains/traffic/data/raw/",

        # INGESTED / CLEANED
        "processed":
            BASE_DIR +
            "/domains/traffic/data/processed/",

        # VALIDATED DATA
        "validated":
            BASE_DIR +
            "/domains/traffic/data/validated/",

        # KPI OUTPUTS
        "kpi":
            BASE_DIR +
            "/domains/traffic/data/kpi/",

        # FEATURE ENGINEERING
        "features":
            BASE_DIR +
            "/domains/traffic/data/features/",

        # MODEL PREDICTIONS
        "predictions":
            BASE_DIR +
            "/domains/traffic/data/predictions/",

        # SIGNALS
        "signals":
            BASE_DIR +
            "/domains/traffic/signals/"
    },

    # =====================================================
    # CROWD DOMAIN
    # =====================================================

    "crowd": {

        "raw":
            BASE_DIR +
            "/domains/crowd/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/crowd/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/crowd/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/crowd/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/crowd/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/crowd/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/crowd/signals/"
    },

    # =====================================================
    # HEALTH DOMAIN
    # =====================================================

    "health": {

        "raw":
            BASE_DIR +
            "/domains/health/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/health/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/health/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/health/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/health/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/health/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/health/signals/"
    },

    # =====================================================
    # TOURISM DOMAIN
    # =====================================================

    "tourism": {

        "raw":
            BASE_DIR +
            "/domains/tourism/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/tourism/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/tourism/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/tourism/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/tourism/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/tourism/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/tourism/signals/"
    },

    # =====================================================
    # GOVERNANCE DOMAIN
    # =====================================================

    "governance": {

        "raw":
            BASE_DIR +
            "/domains/governance/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/governance/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/governance/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/governance/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/governance/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/governance/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/governance/signals/"
    },

    # =====================================================
    # ENVIRONMENT DOMAIN
    # =====================================================

    "environment": {

        "raw":
            BASE_DIR +
            "/domains/environment/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/environment/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/environment/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/environment/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/environment/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/environment/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/environment/signals/"
    },

    # =====================================================
    # SYSTEM LAYER
    # =====================================================

    "system": {

        # GLOBAL SIGNALS
        "signals":
            BASE_DIR +
            "/system/signals/",

        # DEPENDENCY GRAPH
        "graph":
            BASE_DIR +
            "/system/graph/",

        # PIPELINE STATE
        "state":
            BASE_DIR +
            "/system/state/",

        # AI LAYER
        "ai":
            BASE_DIR +
            "/system/ai/",

        # ORCHESTRATION
        "orchestration":
            BASE_DIR +
            "/system/orchestration/"
    }
}

# ============================================
# AUTO-CREATE DIRECTORIES
# ============================================

for domain in PATHS.values():

    for path in domain.values():

        os.makedirs(path, exist_ok=True)

print("All project paths initialized ✅")