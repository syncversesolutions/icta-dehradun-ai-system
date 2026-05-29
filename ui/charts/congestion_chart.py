import plotly.express as px
import pandas as pd


def render_congestion_chart():

    df = pd.DataFrame({

        "time": ["10AM", "11AM", "12PM", "1PM", "2PM"],

        "congestion": [0.42, 0.55, 0.67, 0.81, 0.76]

    })

    fig = px.line(
        df,
        x="time",
        y="congestion",
        title="Congestion Trend"
    )

    return fig