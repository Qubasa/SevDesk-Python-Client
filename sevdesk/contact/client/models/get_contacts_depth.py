from enum import Enum


class GetContactsDepth(str, Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
