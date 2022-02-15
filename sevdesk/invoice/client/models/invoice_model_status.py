from enum import Enum


class InvoiceModelStatus(str, Enum):
    VALUE_0 = "50"
    VALUE_1 = "100"
    VALUE_2 = "200"
    VALUE_3 = "1000"

    def __str__(self) -> str:
        return str(self.value)
