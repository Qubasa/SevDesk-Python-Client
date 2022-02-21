from typing import Union

import attrs

from .. import Client
from ..common import UNSET, Unset
from .client.models import SaveInvoiceInvoicePosObject
from .unity import Unity
from .discount import Discount


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

    def get_api_model(self, client: Client) -> SaveInvoiceInvoicePosObject:
        return SaveInvoiceInvoicePosObject(
            name=self.name,
            quantity=self.quantity,
            tax_rate=self.tax,
            price=self.price,
            discounted_value=self.discount.value if self.discount else UNSET,
            unity=self.unity.get_api_model(client),
            is_percentage=self.discount.percentage if self.discount else UNSET,
        )
