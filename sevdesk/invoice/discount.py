import attrs


@attrs.define()
class Discount:
    value: float
    "The value of discount"
    percentage: bool
    "True if discount is given in percent"
    text: str = "Rabatt"
    "A text shown on the invoice if possible"
