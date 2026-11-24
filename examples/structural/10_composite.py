"""
Composite

Intent: compose objects into tree structures and treat individual leaves and whole branches through the same interface.

Category: Structural
"""

class Node:
    def size(self) -> int: ...

class File(Node):
    def __init__(self, name, bytes_):
        self.name, self.bytes_ = name, bytes_
    def size(self): return self.bytes_

class Folder(Node):
    def __init__(self, name):
        self.name, self.children = name, []
    def add(self, node):
        self.children.append(node)
        return self
    def size(self):
        return sum(child.size() for child in self.children)

root = (Folder("src")
        .add(File("main.py", 1200))
        .add(Folder("lib").add(File("util.py", 800))
                            .add(File("io.py", 400))))

print(root.size())   # 2400 — one call, whole tree
