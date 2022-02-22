from typing import Union

import attrs

from .. import Client
from ..common import UNSET, Unset
from .client.models import SaveInvoiceInvoicePosObject
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
    text: str = ""
    "An optional text descriping the item"
    id: Union[Unset, int] = UNSET
    "The SevDesk internal id"

    def get_api_model(self, client: Client) -> SaveInvoiceInvoicePosObject:
        return SaveInvoiceInvoicePosObject(
            id=self.id,
            name=self.name,
            quantity=self.quantity,
            tax_rate=self.tax,
            price=self.price,
            discounted_value=self.discount.value if self.discount else UNSET,
            unity=self.unity.get_api_model(client),
            is_percentage=self.discount.percentage if self.discount else UNSET,
        )
