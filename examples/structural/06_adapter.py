"""
Adapter

Intent: convert one interface into another that the caller expects, so incompatible code can collaborate.

Category: Structural
"""

class LegacyPrinter:                 # cannot be modified
    def print_old(self, text):
        print(f"[legacy] {text}")

class Printer:                       # what our code expects
    def print(self, text: str) -> None: ...

class PrinterAdapter(Printer):
    def __init__(self, legacy: LegacyPrinter):
        self._legacy = legacy

    def print(self, text: str) -> None:
        self._legacy.print_old(text.upper())

def send_receipt(printer: Printer):
    printer.print("order 1042 confirmed")

send_receipt(PrinterAdapter(LegacyPrinter()))
