from enum import Enum


class VoucherModelRecurringInterval(str, Enum):
    P0Y0M1W = "P0Y0M1W"
    P0Y0M2W = "P0Y0M2W"
    P0Y1M0W = "P0Y1M0W"
    P0Y3M0W = "P0Y3M0W"
    P0Y6M0W = "P0Y6M0W"
    P1Y0M0W = "P1Y0M0W"
    P2Y0M0W = "P2Y0M0W"
    P3Y0M0W = "P3Y0M0W"
    P4Y0M0W = "P4Y0M0W"
    P5Y0M0W = "P5Y0M0W"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
