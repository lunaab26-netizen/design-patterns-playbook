"""
Bridge

Intent: split an abstraction from its implementation so the two can vary independently instead of multiplying into a class per combination.

Category: Structural
"""

from abc import ABC, abstractmethod

class Renderer(ABC):                       # implementation axis
    @abstractmethod
    def circle(self, r: int) -> str: ...

class VectorRenderer(Renderer):
    def circle(self, r): return f"<circle r='{r}'/>"

class RasterRenderer(Renderer):
    def circle(self, r): return f"pixels for r={r}"

class Shape:                               # abstraction axis
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

class Circle(Shape):
    def __init__(self, renderer, r):
        super().__init__(renderer)
        self.r = r
    def draw(self): return self.renderer.circle(self.r)

print(Circle(VectorRenderer(), 10).draw())
print(Circle(RasterRenderer(), 10).draw())
