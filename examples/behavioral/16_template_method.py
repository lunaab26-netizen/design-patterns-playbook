"""
Template Method

Intent: define the skeleton of an algorithm in a base class, letting subclasses override individual steps without changing the order.

Category: Behavioral
"""

from abc import ABC, abstractmethod

class Pipeline(ABC):
    def run(self):                     # the template — final by convention
        raw = self.extract()
        clean = self.transform(raw)
        self.load(clean)

    @abstractmethod
    def extract(self): ...

    @abstractmethod
    def transform(self, raw): ...

    def load(self, rows):              # hook with a sensible default
        print(f"loaded {len(rows)} rows")

class CsvPipeline(Pipeline):
    def extract(self): return ["a,1", "b,2"]
    def transform(self, raw): return [line.split(",") for line in raw]

class ApiPipeline(Pipeline):
    def extract(self): return [{"id": 1}, {"id": 2}]
    def transform(self, raw): return [r["id"] for r in raw]

CsvPipeline().run()   # loaded 2 rows
ApiPipeline().run()   # loaded 2 rows
