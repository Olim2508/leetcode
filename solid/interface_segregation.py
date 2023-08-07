"""
Clients should not be forced to depend upon methods that they do not use.
Interfaces belong to clients, not to hierarchies.
"""

from abc import ABC, abstractmethod

"""
Bad approach. In this example OldPrinter is dependant of fax and scan abstract methods that it does not support. 
"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")


class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
Good approach example. We created 3 separate 
interfaces and inherited them to printers that have methods that printers support
"""


class APrinter(ABC):
    @abstractmethod
    def print(self, document):
        pass


class AFax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class AScanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class AnOldPrinter(APrinter):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class ANewPrinter(APrinter, AFax, AScanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
