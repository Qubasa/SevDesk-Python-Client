from enum import Enum


class CheckAccountResponseModelType(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    REGISTER = "register"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
