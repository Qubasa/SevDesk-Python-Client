from enum import IntEnum


class CheckAccountTransactionUpdateModelStatus(IntEnum):
    VALUE_100 = 100
    VALUE_200 = 200
    VALUE_300 = 300
    VALUE_400 = 400

    def __str__(self) -> str:
        return str(self.value)
