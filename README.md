# Design Patterns Playbook

A working reference for the 18 design patterns you actually reach for in day-to-day
software work — each with a runnable Python 3.11 example, the trigger that tells you
to use it, and the cost you pay for it.

**Read it as a page:** open [`index.html`](index.html) in a browser — filterable,
with a symptom-first decision table and a "when not to" section.

**Read it as code:** every example is a standalone script. No dependencies, no
imports beyond the standard library.

```bash
python3 examples/creational/01_singleton.py
```

## Contents


### Creational

| # | Pattern | Example |
|---|---------|---------|
| 01 | Singleton | [`01_singleton.py`](examples/creational/01_singleton.py) |
| 02 | Factory Method | [`02_factory_method.py`](examples/creational/02_factory_method.py) |
| 03 | Abstract Factory | [`03_abstract_factory.py`](examples/creational/03_abstract_factory.py) |
| 04 | Builder | [`04_builder.py`](examples/creational/04_builder.py) |
| 05 | Prototype | [`05_prototype.py`](examples/creational/05_prototype.py) |

### Structural

| # | Pattern | Example |
|---|---------|---------|
| 06 | Adapter | [`06_adapter.py`](examples/structural/06_adapter.py) |
| 07 | Decorator | [`07_decorator.py`](examples/structural/07_decorator.py) |
| 08 | Facade | [`08_facade.py`](examples/structural/08_facade.py) |
| 09 | Proxy | [`09_proxy.py`](examples/structural/09_proxy.py) |
| 10 | Composite | [`10_composite.py`](examples/structural/10_composite.py) |
| 11 | Bridge | [`11_bridge.py`](examples/structural/11_bridge.py) |

### Behavioral

| # | Pattern | Example |
|---|---------|---------|
| 12 | Strategy | [`12_strategy.py`](examples/behavioral/12_strategy.py) |
| 13 | Observer | [`13_observer.py`](examples/behavioral/13_observer.py) |
| 14 | Command | [`14_command.py`](examples/behavioral/14_command.py) |
| 15 | State | [`15_state.py`](examples/behavioral/15_state.py) |
| 16 | Template Method | [`16_template_method.py`](examples/behavioral/16_template_method.py) |
| 17 | Iterator | [`17_iterator.py`](examples/behavioral/17_iterator.py) |
| 18 | Chain of Responsibility | [`18_chain.py`](examples/behavioral/18_chain.py) |

## How to use this

The decision table in the playbook starts from the **symptom**, not the pattern name —
"my constructor takes nine arguments", "I need undo/redo", "I keep adding an `if` for
each new type". That is the direction you actually arrive from. Find your symptom,
then read the pattern it points at.

Each example file carries a docstring with the intent, and a `# Watch out:` note at the
bottom where the naive version has a real trap (Singleton and Prototype both do).

## A word on over-engineering

Patterns are vocabulary for problems you already have, not a checklist to apply.
The playbook's "When not to" section is the most important page in it: most of these
patterns exist to remove a specific kind of pain, and if you do not have that pain,
the pattern is pure cost. Two of the most common failure modes are wrapping a
three-line function in a Strategy hierarchy, and introducing an Abstract Factory for
a family that will only ever have one member.

## Verification

All 18 examples were executed with Python 3.11 and exit cleanly. The page was checked
for structure, script parsing, asset reachability and headless render at desktop and
390px width.

## License

MIT — see [LICENSE](LICENSE).
