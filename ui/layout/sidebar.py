import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():

    with st.sidebar:

        selected = option_menu(

            "ICTA Operations",

            [
                "Overview",
                "Traffic",
                "Crowd",
                "Accommodation",
                "Predictions",
                "AI Operations"
            ],

            icons=[
                "speedometer2",
                "sign-turn-right",
                "people",
                "house",
                "graph-up",
                "cpu"
            ],

            default_index=0
        )

    return selected