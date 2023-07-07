from enum import IntEnum


class CheckAccountModelStatus(IntEnum):
    VALUE_0 = 0
    VALUE_100 = 100

    def __str__(self) -> str:
        return str(self.value)
