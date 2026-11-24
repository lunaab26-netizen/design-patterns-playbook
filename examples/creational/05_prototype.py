"""
Prototype

Intent: create new objects by cloning an existing configured instance instead of re-running its construction.

Category: Creational
"""

import copy

class Document:
    def __init__(self, title, blocks):
        self.title = title
        self.blocks = blocks

    def clone(self):
        return copy.deepcopy(self)   # nested blocks are copied too

base = Document("Quarterly Report", [{"type": "h1", "text": "Q3"}])

draft = base.clone()
draft.blocks.append({"type": "p", "text": "Revenue up 12%"})

print(len(base.blocks))    # 1  — original untouched
print(len(draft.blocks))   # 2

# Watch out: copy.copy() shares the nested list — mutating the clone would silently mutate the original. Use deepcopy unless you have proven sharing is safe.
