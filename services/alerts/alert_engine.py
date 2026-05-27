def generate_alerts(signals):

    alerts = []

    for signal in signals:

        if signal["signal"] == "congestion" and signal["value"] > 0.8:

            alerts.append({

                "severity": "critical",

                "title": "Critical Congestion",

                "location": signal["location"],

                "message":
                    "Traffic congestion crossing safe threshold."

            })

    return alerts