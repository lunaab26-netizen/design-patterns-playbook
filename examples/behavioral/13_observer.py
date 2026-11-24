"""
Observer

Intent: let objects subscribe to changes in another object, so the publisher never needs to know who is listening.

Category: Behavioral
"""

class EventBus:
    def __init__(self):
        self._subs = {}

    def subscribe(self, event, fn):
        self._subs.setdefault(event, []).append(fn)
        return lambda: self._subs[event].remove(fn)   # unsubscribe

    def publish(self, event, payload):
        for fn in list(self._subs.get(event, [])):
            fn(payload)

bus = EventBus()
off = bus.subscribe("order.paid", lambda o: print("ship", o["id"]))
bus.subscribe("order.paid", lambda o: print("email receipt", o["id"]))

bus.publish("order.paid", {"id": 42})
off()                                   # stop listening
bus.publish("order.paid", {"id": 43})   # only the email fires
