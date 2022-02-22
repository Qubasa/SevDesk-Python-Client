from enum import Enum


class InvoiceModelSendType(str, Enum):
    VPR = "VPR"
    VPDF = "VPDF"
    VM = "VM"
    VP = "VP"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
