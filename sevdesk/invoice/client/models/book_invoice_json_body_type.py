from enum import Enum


class BookInvoiceJsonBodyType(str, Enum):
    N = "N"
    CB = "CB"
    CF = "CF"
    O = "O"
    OF = "OF"
    MTC = "MTC"

    def __str__(self) -> str:
        return str(self.value)
