from datetime import datetime


class RealtimeMonitor:

    def __init__(self):

        self.metrics = {

            "events_processed":
                0,

            "critical_signals":
                0,

            "active_streams":
                0,

            "last_update":
                None
        }

    # ========================================
    # UPDATE METRICS
    # ========================================

    def update_metrics(

        self,
        events=0,
        critical=0,
        streams=0

    ):

        self.metrics[
            "events_processed"
        ] += events

        self.metrics[
            "critical_signals"
        ] += critical

        self.metrics[
            "active_streams"
        ] = streams

        self.metrics[
            "last_update"
        ] = str(datetime.now())

    # ========================================
    # DISPLAY METRICS
    # ========================================

    def display_metrics(self):

        print("\n")
        print("=" * 60)

        print("ICTA REALTIME MONITOR")

        print("=" * 60)

        for key, value in self.metrics.items():

            print(f"\n{key}:")
            print(value)

        print("\n")
        print("=" * 60)