"""
State

Intent: let an object change its behaviour when its internal state changes, by delegating to a state object instead of branching on a status field.

Category: Behavioral
"""

class Order:
    ALLOWED = {
        "pending": {"pay": "paid", "cancel": "cancelled"},
        "paid":    {"ship": "shipped", "refund": "refunded"},
        "shipped": {"deliver": "delivered"},
    }

    def __init__(self):
        self.state = "pending"

    def _move(self, action):
        nxt = self.ALLOWED.get(self.state, {}).get(action)
        if nxt is None:
            raise ValueError(f"cannot {action} from {self.state}")
        self.state = nxt
        return self

    def pay(self):    return self._move("pay")
    def ship(self):   return self._move("ship")
    def cancel(self): return self._move("cancel")

o = Order().pay().ship()
print(o.state)          # shipped
try:
    o.cancel()          # illegal from shipped
except ValueError as e:
    print(e)

# Watch out: This table-driven form is the pragmatic version. Switch to real state objects only when each state carries its own data or many methods.
