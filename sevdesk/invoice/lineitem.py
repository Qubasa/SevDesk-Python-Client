from __future__ import annotations

from typing import Union

import attrs

from .. import Client
from ..common import UNSET, Unset
from .client.models import InvoicePositionModel, SaveInvoiceInvoicePosObject
from .discount import Discount
from .unity import Unity


@attrs.define()
class LineItem:
    name: str
    "The name"
    quantity: float
    "Quantity of the item"
    price: float
    "The price of the item. You can either specify prices in gross or net, depending on the invoice settings. Be careful not to mix things."
    tax: float
    "The tax-rate of the item"
    unity: Unity = Unity.PIECE
    "The unity of the item"
    discount: Union[Unset, Discount] = UNSET
    "An optional discount"
    text: Union[Unset, str] = UNSET
    "An optional text descriping the item"
    id: Union[Unset, int] = UNSET
    "The SevDesk internal id"

    def _get_api_model(self, client: Client) -> SaveInvoiceInvoicePosObject:
        return SaveInvoiceInvoicePosObject(
            id=self.id,
            name=self.name,
            quantity=self.quantity,
            tax_rate=self.tax,
            price=self.price,
            discounted_value=self.discount.value if self.discount else UNSET,
            unity=self.unity._get_api_model(client),
            is_percentage=self.discount.percentage if self.discount else UNSET,
            text=self.text,
        )

    @classmethod
    def _from_model(cls, client: Client, model: InvoicePositionModel) -> LineItem:
        return cls(
            name=model.name,
            quantity=float(model.quantity),
            price=float(model.price),
            tax=float(model.tax_rate),
            unity=Unity(model.unity.translation_code),
            discount=Discount(
                value=float(model.discounted_value),
                percentage=bool(int(model.is_percentage)),
            )
            if model.discounted_value is not None
            else UNSET,
            text=model.text if model.text is not None else UNSET,
            id=int(model.id),
        )
