"""
Command

Intent: turn a request into a standalone object, so it can be queued, logged, retried, or undone.

Category: Behavioral
"""

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...

class AddText(Command):
    def __init__(self, doc, text):
        self.doc, self.text = doc, text
    def execute(self): self.doc.append(self.text)
    def undo(self): self.doc.pop()

class History:
    def __init__(self): self._done = []
    def run(self, cmd):
        cmd.execute()
        self._done.append(cmd)
    def undo(self):
        if self._done:
            self._done.pop().undo()

doc, history = [], History()
history.run(AddText(doc, "hello"))
history.run(AddText(doc, "world"))
print(doc)          # ['hello', 'world']
history.undo()
print(doc)          # ['hello']
