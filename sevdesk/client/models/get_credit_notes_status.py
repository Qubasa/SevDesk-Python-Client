from enum import Enum


class GetCreditNotesStatus(str, Enum):
    VALUE_0 = "100"
    VALUE_1 = "200"
    VALUE_2 = "1000"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
