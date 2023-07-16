from enum import Enum


class VoucherModelCreditDebit(str, Enum):
    C = "C"
    D = "D"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
