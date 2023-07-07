from enum import Enum


class CheckAccountModelType(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
