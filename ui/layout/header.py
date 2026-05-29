import streamlit as st
from datetime import datetime


def render_header():

    st.markdown(f"""

    # ICTA Yatra Intelligence Platform

    ### Live Operational Command Center

    *System Status:* Operational  
    *AI Engine:* Active  
    *Time:* {datetime.now().strftime("%H:%M:%S")}

    """)