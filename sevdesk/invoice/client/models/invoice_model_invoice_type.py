from enum import Enum


class InvoiceModelInvoiceType(str, Enum):
    RE = "RE"
    WKR = "WKR"
    SR = "SR"
    MA = "MA"
    TR = "TR"
    ER = "ER"

    def __str__(self) -> str:
        return str(self.value)
