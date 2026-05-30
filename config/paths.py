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
    # Raw Data
    # =====================================================

    "data": {
        
        "raw":
          BASE_DIR +
          "/data/raw/"
    },

    # =====================================================
    # TRAFFIC DOMAIN
    # =====================================================

    "traffic": {

        "raw":
            BASE_DIR +
            "/domains/traffic/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/traffic/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/traffic/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/traffic/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/traffic/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/traffic/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/traffic/signals/",

        "modules":
            BASE_DIR +
            "/domains/traffic/modules/",

        "pipelines":
            BASE_DIR +
            "/domains/traffic/pipelines/"
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
    # ACCOMMODATION DOMAIN
    # =====================================================

    "accommodation": {

    "raw":
        BASE_DIR +
        "/domains/accommodation/data/raw/",

    "processed":
        BASE_DIR +
        "/domains/accommodation/data/processed/",

    "validated":
        BASE_DIR +
        "/domains/accommodation/data/validated/",

    "kpi":
        BASE_DIR +
        "/domains/accommodation/data/kpi/",

    "features":
        BASE_DIR +
        "/domains/accommodation/data/features/",

    "predictions":
        BASE_DIR +
        "/domains/accommodation/data/predictions/",

    "signals":
        BASE_DIR +
        "/domains/accommodation/signals/",

    "modules":
        BASE_DIR +
        "/domains/accommodation/modules/",

    "pipelines":
        BASE_DIR +
        "/domains/accommodation/pipelines/"
},

    # =====================================================
    # WEATHER DOMAIN
    # =====================================================

    "weather": {

        "raw":
            BASE_DIR +
            "/domains/weather/data/raw/",

        "processed":
            BASE_DIR +
            "/domains/weather/data/processed/",

        "validated":
            BASE_DIR +
            "/domains/weather/data/validated/",

        "kpi":
            BASE_DIR +
            "/domains/weather/data/kpi/",

        "features":
            BASE_DIR +
            "/domains/weather/data/features/",

        "predictions":
            BASE_DIR +
            "/domains/weather/data/predictions/",

        "signals":
            BASE_DIR +
            "/domains/weather/signals/"
    },

    # =====================================================
    # SYSTEM LAYER
    # =====================================================

    "system": {

        "signals":
            BASE_DIR +
            "/system/signals/",

        "graph":
            BASE_DIR +
            "/system/graph/",

        "state":
            BASE_DIR +
            "/system/state/",

        "ai":
            BASE_DIR +
            "/system/ai/",

        "orchestration":
            BASE_DIR +
            "/system/orchestration/",

        "events":
            BASE_DIR +
            "/system/events/",

    },

    # =====================================================
    # APP LAYER
    # =====================================================

    "app": {

        "root":
            BASE_DIR +
            "/app/"
    },

    # =====================================================
    # CORE LAYER
    # =====================================================

    "core": {

        "config":
            BASE_DIR +
            "/core/config/",

        "routing":
            BASE_DIR +
            "/core/routing/",

        "state":
            BASE_DIR +
            "/core/state/",

        "realtime":
            BASE_DIR +
            "/core/realtime/"
    },

    # =====================================================
    # UI LAYER
    # =====================================================

    "ui": {

        "themes":
            BASE_DIR +
            "/ui/themes/",

        "layout":
            BASE_DIR +
            "/ui/layout/",

        "cards":
            BASE_DIR +
            "/ui/cards/",

        "charts":
            BASE_DIR +
            "/ui/charts/",

        "maps":
            BASE_DIR +
            "/ui/maps/"
    },

    # =====================================================
    # DASHBOARD LAYER
    # =====================================================

    "dashboards": {

        "overview":
            BASE_DIR +
            "/dashboards/overview/",

        "traffic":
            BASE_DIR +
            "/dashboards/traffic/",

        "crowd":
            BASE_DIR +
            "/dashboards/crowd/",

        "accommodation":
            BASE_DIR +
            "/dashboards/accommodation/",

        "predictions":
            BASE_DIR +
            "/dashboards/predictions/",

        "ai_ops":
            BASE_DIR +
            "/dashboards/ai_ops/"
    },

    # =====================================================
    # SERVICES LAYER
    # =====================================================

    "services": {

        "signals":
            BASE_DIR +
            "/services/signals/",

        "alerts":
            BASE_DIR +
            "/services/alerts/",

        "aggregation":
            BASE_DIR +
            "/services/aggregation/",

        "orchestration":
            BASE_DIR +
            "/services/orchestration/"
    },

    # =====================================================
    # AI LAYER
    # =====================================================

    "ai": {

        "recommendation":
            BASE_DIR +
            "/ai/recommendation/",

        "reasoning":
            BASE_DIR +
            "/ai/reasoning/",

        "prediction":
            BASE_DIR +
            "/ai/prediction/",

        "simulation":
            BASE_DIR +
            "/ai/simulation/"
    },

    # =====================================================
    # ASSETS
    # =====================================================

    "assets": {

        "icons":
            BASE_DIR +
            "/assets/icons/",

        "logos":
            BASE_DIR +
            "/assets/logos/",

        "backgrounds":
            BASE_DIR +
            "/assets/backgrounds/",

        "lottie":
            BASE_DIR +
            "/assets/lottie/"
    }
}

# ============================================
# AUTO-CREATE DIRECTORIES
# ============================================

for section in PATHS.values():

    for path in section.values():

        os.makedirs(path, exist_ok=True)

print("All project paths initialized ✅")