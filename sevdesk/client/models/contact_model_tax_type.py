from enum import Enum


class ContactModelTaxType(str, Enum):
    DEFAULT = "default"
    EU = "eu"
    NOTEU = "noteu"
    CUSTOM = "custom"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
