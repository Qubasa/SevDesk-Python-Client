from enum import Enum


class CheckAccountTransactionResponseModelStatus(str, Enum):
    VALUE_0 = "100"
    VALUE_1 = "200"
    VALUE_2 = "300"
    VALUE_3 = "350"
    VALUE_4 = "400"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
