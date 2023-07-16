from enum import IntEnum


class VoucherResponseModelStatus(IntEnum):
    VALUE_50 = 50
    VALUE_100 = 100
    VALUE_1000 = 1000

    def __str__(self) -> str:
        return str(self.value)
