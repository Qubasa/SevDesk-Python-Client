from enum import Enum


class InvoiceModelSendType(str, Enum):
    VPR = "VPR"
    VPDF = "VPDF"
    VM = "VM"
    VP = "VP"

    def __str__(self) -> str:
        return str(self.value)
