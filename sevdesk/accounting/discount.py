from __future__ import annotations

from typing import TypeVar, Union

import attrs

from .. import UNSET, Client, Unset
from ..client.models import DiscountPositionModel

T = TypeVar("T")


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

    def _get_api_model(self, client: Client, t: T) -> T:
        return t(
            id=self.id,
            discount=True,
            text=self.text,
            percentage=self.percentage,
            value=self.value,
        )

    @classmethod
    def _from_model(cls, client: Client, model: DiscountPositionModel) -> Discount:
        return cls(
            id=int(model.id),
            text=model.text,
            percentage=bool(model.percentage),
            value=float(model.value),
        )
