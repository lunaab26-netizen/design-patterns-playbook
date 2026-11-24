"""
Singleton

Intent: guarantee exactly one instance of a class and give it a single, global access point.

Category: Creational
"""

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {"env": "prod", "retries": 3}
        return cls._instance

cfg = Config()
assert Config() is cfg          # same object, every time
print(cfg.settings["env"])      # prod

# Watch out: In Python a module-level instance (config = Config()) is usually the better answer — it is a singleton the language already enforces. Use the class form only when you need lazy construction.
