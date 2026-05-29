import pydeck as pdk
import streamlit as st
import pandas as pd


def render_traffic_map():

    data = pd.DataFrame({

        "lat": [30.3165, 30.4894],

        "lon": [78.0322, 79.2153],

        "congestion": [80, 95]

    })

    st.pydeck_chart(pdk.Deck(

        map_style="mapbox://styles/mapbox/dark-v10",

        initial_view_state=pdk.ViewState(
            latitude=30.3165,
            longitude=78.0322,
            zoom=7,
            pitch=50,
        ),

        layers=[

            pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position='[lon, lat]',
                get_radius=2000,
                get_fill_color='[255, 0, 0, 160]',
                pickable=True,
            ),

        ],
    ))