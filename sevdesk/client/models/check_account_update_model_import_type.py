from enum import Enum


class CheckAccountUpdateModelImportType(str, Enum):
    CSV = "CSV"
    MT940 = "MT940"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
