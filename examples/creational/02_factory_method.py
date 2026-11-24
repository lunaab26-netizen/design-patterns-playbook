"""
Factory Method

Intent: let a function or subclass decide which concrete class to instantiate, so callers depend on an interface rather than a constructor.

Category: Creational
"""

from abc import ABC, abstractmethod
import json

class Exporter(ABC):
    @abstractmethod
    def export(self, rows): ...

class CsvExporter(Exporter):
    def export(self, rows):
        return "\n".join(",".join(map(str, r)) for r in rows)

class JsonExporter(Exporter):
    def export(self, rows):
        return json.dumps(rows)

def make_exporter(fmt: str) -> Exporter:
    registry = {"csv": CsvExporter, "json": JsonExporter}
    if fmt not in registry:
        raise ValueError(f"unknown format: {fmt}")
    return registry[fmt]()

print(make_exporter("csv").export([(1, "a"), (2, "b")]))
