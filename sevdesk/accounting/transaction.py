import attrs


@attrs.define()
class Transaction:
    gateway: str
    "The name of the gateway"
    amount: float
    "Amount paid by this transaction"
    voucher: bool = False
    "True if this transaction is a voucher"
