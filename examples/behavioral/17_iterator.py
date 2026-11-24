"""
Iterator

Intent: expose a way to walk a collection's elements one at a time, without revealing how the collection is stored.

Category: Behavioral
"""

class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __iter__(self):                 # depth-first, lazy
        yield self.value
        for child in self.children:
            yield from child

root = Tree("a", [Tree("b", [Tree("d")]), Tree("c")])

for node in root:
    print(node)          # a b d c

print(list(root))        # ['a', 'b', 'd', 'c']
