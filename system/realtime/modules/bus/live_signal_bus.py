from datetime import datetime


class LiveSignalBus:

    def __init__(self):

        self.signal_stream = []

    # ========================================
    # PUBLISH SIGNAL
    # ========================================

    def publish_signal(

        self,
        signal

    ):

        signal["published_at"] = (
            str(datetime.now())
        )

        self.signal_stream.append(
            signal
        )

        print("\nSignal published ✅")

    # ========================================
    # GET STREAM
    # ========================================

    def get_stream(self):

        return self.signal_stream

    # ========================================
    # DISPLAY STREAM
    # ========================================

    def display_stream(self):

        print("\n")
        print("=" * 60)

        print("LIVE SIGNAL BUS")

        print("=" * 60)

        for signal in self.signal_stream:

            print("\n", signal)

        print("\n")
        print("=" * 60)