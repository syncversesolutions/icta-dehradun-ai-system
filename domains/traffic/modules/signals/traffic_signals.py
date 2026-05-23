# ============================================
# IMPORTS
# ============================================

import json

# ============================================
# GENERATE TRAFFIC SIGNALS
# ============================================

def generate_traffic_signals(df):

    signals = []

    for _, row in df.iterrows():

        risk_level = row[
            "predicted_risk_level"
        ]

        # ============================================
        # SIGNAL RULES
        # ============================================

        if risk_level == "Severe":

            signal = {

                "domain": "traffic",

                "signal_type":
                    "critical_congestion",

                "route_id":
                    row["route_id"],

                "checkpoint_name":
                    row["checkpoint_name"],

                "risk_level":
                    risk_level,

                "predicted_score":
                    float(
                        row[
                            "predicted_congestion_score"
                        ]
                    ),

                "recommended_action":
                    "Immediate rerouting required"
            }

            signals.append(signal)

        elif risk_level == "High":

            signal = {

                "domain": "traffic",

                "signal_type":
                    "high_congestion",

                "route_id":
                    row["route_id"],

                "checkpoint_name":
                    row["checkpoint_name"],

                "risk_level":
                    risk_level,

                "predicted_score":
                    float(
                        row[
                            "predicted_congestion_score"
                        ]
                    ),

                "recommended_action":
                    "Increase traffic monitoring"
            }

            signals.append(signal)

    return signals

# ============================================
# SAVE SIGNALS
# ============================================

def save_signals(
    signals,
    output_path
):

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(

            signals,
            file,
            indent=4
        )

    print(
        f"\nSignals saved at:"
    )

    print(output_path)