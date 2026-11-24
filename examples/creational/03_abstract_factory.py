"""
Abstract Factory

Intent: create whole families of related objects that must be used together, without naming their concrete classes.

Category: Creational
"""

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...

class DarkButton(Button):
    def render(self): return "[ Dark Button ]"

class LightButton(Button):
    def render(self): return "[ Light Button ]"

class ThemeFactory(ABC):
    @abstractmethod
    def button(self) -> Button: ...

class DarkTheme(ThemeFactory):
    def button(self): return DarkButton()

class LightTheme(ThemeFactory):
    def button(self): return LightButton()

def build_ui(factory: ThemeFactory) -> str:
    return factory.button().render()   # never names a concrete class

print(build_ui(DarkTheme()))   # [ Dark Button ]
