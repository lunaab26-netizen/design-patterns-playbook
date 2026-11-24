"""
Strategy

Intent: define a family of interchangeable algorithms and let the caller pick one at runtime.

Category: Behavioral
"""

from abc import ABC, abstractmethod

class Pricing(ABC):
    @abstractmethod
    def total(self, amount: float) -> float: ...

class FullPrice(Pricing):
    def total(self, amount): return amount

class Seasonal(Pricing):
    def __init__(self, pct): self.pct = pct
    def total(self, amount): return round(amount * (1 - self.pct), 2)

class Member(Pricing):
    def total(self, amount): return round(amount - 5, 2)

class Cart:
    def __init__(self, pricing: Pricing):
        self.pricing = pricing
    def checkout(self, amount):
        return self.pricing.total(amount)

print(Cart(Seasonal(0.20)).checkout(100))   # 80.0
print(Cart(Member()).checkout(100))         # 95.0
