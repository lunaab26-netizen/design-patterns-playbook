"""
Chain of Responsibility

Intent: pass a request along a chain of handlers until one of them deals with it, so the sender never names a receiver.

Category: Behavioral
"""

class Handler:
    def __init__(self, nxt=None):
        self.next = nxt

    def handle(self, req):
        if self.next:
            return self.next.handle(req)
        return "200 OK"          # terminal case

class Auth(Handler):
    def handle(self, req):
        if not req.get("token"):
            return "401 Unauthorized"
        return super().handle(req)

class RateLimit(Handler):
    def handle(self, req):
        if req.get("burst", 0) > 100:
            return "429 Too Many Requests"
        return super().handle(req)

pipeline = Auth(RateLimit())

print(pipeline.handle({"token": "t", "burst": 5}))    # 200 OK
print(pipeline.handle({"burst": 5}))                  # 401 Unauthorized
print(pipeline.handle({"token": "t", "burst": 500}))  # 429 Too Many Requests
