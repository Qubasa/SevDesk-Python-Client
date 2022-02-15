from enum import Enum


class ContactModelTaxType(str, Enum):
    DEFAULT = "default"
    EU = "eu"
    NOTEU = "noteu"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
