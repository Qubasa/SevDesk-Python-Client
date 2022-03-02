from enum import Enum


class CreditNoteBookingCategory(str, Enum):
    PROVISION = "PROVISION"
    ROYALTY_ASSIGNED = "ROYALTY_ASSIGNED"
    ROYALTY_UNASSIGNED = "ROYALTY_UNASSIGNED"
    UNDERACHIEVEMENT = "UNDERACHIEVEMENT"
    ACCOUNTING_TYPE = "ACCOUNTING_TYPE"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
