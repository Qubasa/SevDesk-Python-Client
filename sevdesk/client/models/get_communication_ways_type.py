from enum import Enum


class GetCommunicationWaysType(str, Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"
    WEB = "WEB"
    MOBILE = "MOBILE"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
