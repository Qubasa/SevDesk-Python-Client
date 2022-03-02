from enum import Enum


class CreditNoteCreditNoteType(str, Enum):
    CN = "CN"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
