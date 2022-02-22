from enum import Enum


class InvoiceModelInvoiceType(str, Enum):
    RE = "RE"
    WKR = "WKR"
    SR = "SR"
    MA = "MA"
    TR = "TR"
    ER = "ER"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
