from system.orchestration.signal_router import (
    SignalRouter
)


class StreamProcessor:

    def __init__(self):

        self.router = SignalRouter()

    # ========================================
    # PROCESS SIGNAL STREAM
    # ========================================

    def process_stream(

        self,
        signals

    ):

        print("\n")
        print("=" * 60)

        print("PROCESSING LIVE SIGNAL STREAM")

        print("=" * 60)

        for signal in signals:

            status = signal.get(
                "status",
                "normal"
            )

            if status == "critical":

                print(
                    "\nCritical live signal detected"
                )

                self.router.route_signal(
                    signal
                )

            else:

                print(
                    "\nNormal signal ignored"
                )

        print("\n")
        print("=" * 60)

        print("STREAM PROCESSING COMPLETE")

        print("=" * 60)