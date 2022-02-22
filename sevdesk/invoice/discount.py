from typing import Union

import attrs

from .. import Client
from ..common import UNSET, Unset
from .client.models import SaveInvoiceDiscountSave


@attrs.define()
class Discount:
    value: float
    "The value of discount"
    percentage: bool
    "True if discount is given in percent"
    text: str = "Rabatt"
    "A text shown on the invoice if possible"
    id: Union[Unset, int] = UNSET
    "The SevDesk internal id"

    def get_api_model(self, client: Client) -> SaveInvoiceDiscountSave:
        return SaveInvoiceDiscountSave(
            id=self.id,
            discount=True,
            text=self.text,
            percentage=self.percentage,
            value=self.value,
        )
