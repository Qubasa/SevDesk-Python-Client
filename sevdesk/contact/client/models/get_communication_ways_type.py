from enum import Enum


class GetCommunicationWaysType(str, Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"
    WEB = "WEB"
    MOBILE = "MOBILE"

    def __str__(self) -> str:
        return str(self.value)
