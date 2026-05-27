PRIMARY_BG = "#071028"
SECONDARY_BG = "#0B1736"

CYAN = "#00E5FF"
BLUE = "#3B82F6"

GREEN = "#00FFB3"

WARNING = "#FFB020"
CRITICAL = "#FF4D6D"

PURPLE = "#8B5CF6"


def apply_theme():
    return f"""
    <style>

    .stApp {{
        background-color: {PRIMARY_BG};
        color: white;
    }}

    .metric-card {{
        background: {SECONDARY_BG};
        padding: 20px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 0 20px rgba(0,229,255,0.08);
    }}

    .alert-card {{
        background: rgba(255,77,109,0.1);
        border-left: 4px solid {CRITICAL};
        padding: 16px;
        border-radius: 12px;
    }}

    </style>
    """