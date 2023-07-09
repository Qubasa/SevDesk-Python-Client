from enum import Enum


class ContactResponseModelTaxType(str, Enum):
    DEFAULT = "default"
    EU = "eu"
    NOTEU = "noteu"
    CUSTOM = "custom"
    SS = "ss"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
