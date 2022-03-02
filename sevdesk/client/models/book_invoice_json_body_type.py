from enum import Enum


class BookInvoiceJsonBodyType(str, Enum):
    N = "N"
    CB = "CB"
    CF = "CF"
    O = "O"
    OF = "OF"
    MTC = "MTC"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
