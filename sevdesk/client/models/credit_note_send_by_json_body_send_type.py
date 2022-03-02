from enum import Enum


class CreditNoteSendByJsonBodySendType(str, Enum):
    VPR = "VPR"
    VP = "VP"
    VM = "VM"
    VPDF = "VPDF"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
