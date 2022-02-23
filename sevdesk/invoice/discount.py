from __future__ import annotations

from typing import Union

import attrs

from .. import Client
from ..common import UNSET, Unset
from .client.models import InvoiceDiscountPositionModel, SaveInvoiceDiscountSave


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

    def _get_api_model(self, client: Client) -> SaveInvoiceDiscountSave:
        return SaveInvoiceDiscountSave(
            id=self.id,
            discount=True,
            text=self.text,
            percentage=self.percentage,
            value=self.value,
        )

    @classmethod
    def _from_model(
        cls, client: Client, model: InvoiceDiscountPositionModel
    ) -> Discount:
        return cls(
            id=int(model.id),
            text=model.text,
            percentage=bool(model.percentage),
            value=float(model.value),
        )
