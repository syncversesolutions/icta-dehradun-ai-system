from datetime import datetime


class EventListener:

    def __init__(self):

        self.events = []

    # ========================================
    # RECEIVE EVENT
    # ========================================

    def receive_event(

        self,
        domain,
        event_type,
        payload

    ):

        event = {

            "domain":
                domain,

            "event_type":
                event_type,

            "payload":
                payload,

            "timestamp":
                str(datetime.now())
        }

        self.events.append(event)

        print("\nRealtime event received ✅")

        return event

    # ========================================
    # DISPLAY EVENTS
    # ========================================

    def display_events(self):

        print("\n")
        print("=" * 60)

        print("ICTA REALTIME EVENTS")

        print("=" * 60)

        for event in self.events:

            print("\n", event)

        print("\n")
        print("=" * 60)