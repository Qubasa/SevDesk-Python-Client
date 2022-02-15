from enum import Enum


class InvoiceSendByJsonBodySendType(str, Enum):
    VPR = "VPR"
    VP = "VP"
    VM = "VM"
    VPDF = "VPDF"

    def __str__(self) -> str:
        return str(self.value)
