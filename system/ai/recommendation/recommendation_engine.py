def generate_recommendations(system_state):

    recommendations = []

    congestion = system_state["traffic"]["congestion"]

    if congestion > 0.8:

        recommendations.append({

            "title": "Restrict Inflow",

            "reason":
                "High congestion detected near Kedarnath route.",

            "impact":
                "Reduce downstream pressure",

            "confidence": 0.91

        })

    return recommendations