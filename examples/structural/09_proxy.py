"""
Proxy

Intent: stand in for another object to control access to it — lazily, cheaply, or with a permission check.

Category: Structural
"""

class RealImage:
    def __init__(self, path):
        self.path = path
        print(f"loading {path} from disk…")   # expensive

    def display(self):
        return f"showing {self.path}"

class LazyImage:                              # proxy
    def __init__(self, path):
        self.path = path
        self._real = None

    def display(self):
        if self._real is None:
            self._real = RealImage(self.path)  # built on first use
        return self._real.display()

img = LazyImage("cover.png")   # nothing loaded yet
print(img.display())           # loads, then shows
print(img.display())           # reuses the instance
