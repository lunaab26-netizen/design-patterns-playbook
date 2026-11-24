"""
Decorator

Intent: attach responsibilities to an object at runtime by wrapping it, instead of subclassing every combination.

Category: Structural
"""

import functools, time

def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            ms = (time.perf_counter() - start) * 1000
            print(f"{fn.__name__} took {ms:.1f}ms")
    return wrapper

def retried(times=3):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
        return wrapper
    return deco

@timed
@retried(times=3)
def fetch_report(order_id):
    return {"id": order_id, "status": "ok"}

fetch_report(1042)

# Watch out: Decorators apply bottom-up: @timed above @retried means the timer measures all three attempts, not each one. Swap them if you want per-attempt timing.
