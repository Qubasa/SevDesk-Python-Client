from enum import Enum


class CommunicationWayModelType(str, Enum):
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    WEB = "WEB"
    MOBILE = "MOBILE"

    def __str__(self) -> str:
        return str(self.value)
