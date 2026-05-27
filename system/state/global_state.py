import streamlit as st


def initialize_state():

    if "system_state" not in st.session_state:

        st.session_state.system_state = {

            "traffic": {
                "congestion": 0.82,
                "vehicle_density": 0.74,
                "travel_delay": 28,
                "checkpoint_throughput": 71
            },

            "alerts": [],

            "recommendations": [],

            "predictions": {}
        }