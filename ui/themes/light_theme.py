# =========================================================
# ICTA LIGHT COMMAND CENTER THEME
# =========================================================
PRIMARY_BG = "#F5F7FB"
SECONDARY_BG = "#FFFFFF"
CYAN = "#0891B2"
BLUE = "#2563EB"
GREEN = "#10B981"
WARNING = "#F59E0B"
CRITICAL = "#EF4444"
PURPLE = "#7C3AED"
TEXT = "#111827"
MUTED = "#6B7280"
# =========================================================
# APPLY THEME
# =========================================================
def apply_theme():
    return f"""
    <style>
    /* =====================================================
       GLOBAL
    ===================================================== */
    .stApp {{
        background-color: {PRIMARY_BG};
        color: {TEXT};
    }}
    /* =====================================================
       SIDEBAR
    ===================================================== */
    section[data-testid="stSidebar"] {{
        background-color: {SECONDARY_BG};
        border-right:
            1px solid rgba(0,0,0,0.08);
    }}
    /* =====================================================
       METRIC CARDS
    ===================================================== */
    .metric-card {{
        background:
            rgba(255,255,255,0.98);
        padding: 20px;
        border-radius: 16px;
        border:
            1px solid rgba(0,0,0,0.06);
        box-shadow:
            0 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 15px;
    }}
    /* =====================================================
       ALERT CARDS
    ===================================================== */
    .alert-card {{
        background:
            rgba(239,68,68,0.08);
        padding: 16px;
        border-left:
            4px solid {CRITICAL};
        border-radius: 12px;
        margin-bottom: 10px;
    }}
    /* =====================================================
       AI CARDS
    ===================================================== */
    .ai-card {{
        background:
            rgba(124,58,237,0.08);
        padding: 16px;
        border-left:
            4px solid {PURPLE};
        border-radius: 12px;
        margin-bottom: 10px;
    }}
    /* =====================================================
       HEADERS
    ===================================================== */
    h1, h2, h3, h4 {{
        color: {TEXT};
    }}
    /* =====================================================
       BUTTONS
    ===================================================== */
    .stButton > button {{
        background-color: {BLUE};
        color: white;
        border-radius: 10px;
        border: none;
    }}
    /* =====================================================
       TABS
    ===================================================== */
    button[data-baseweb="tab"] {{
        color: {TEXT};
    }}
    /* =====================================================
       SCROLLBAR
    ===================================================== */
    ::-webkit-scrollbar {{
        width: 8px;
    }}
    ::-webkit-scrollbar-thumb {{
        background: {BLUE};
        border-radius: 8px;
    }}
    </style>
    """