from enum import Enum


class GetInvoicesStatus(str, Enum):
    VALUE_0 = "100"
    VALUE_1 = "200"
    VALUE_2 = "1000"

    def __str__(self) -> str:
        return str(self.value)
