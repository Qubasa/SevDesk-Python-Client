from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceDiscountPositionModel")


@attr.s(auto_attribs=True)
class InvoiceDiscountPositionModel:
    """Invoice discount model

    Attributes:
        id (Union[Unset, int]): The invoice discount id
        text (Union[Unset, None, str]):
        percentage (Union[Unset, None, bool]):
        value (Union[Unset, None, float]):
    """

    id: Union[Unset, int] = UNSET
    text: Union[Unset, None, str] = UNSET
    percentage: Union[Unset, None, bool] = UNSET
    value: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        text = self.text
        percentage = self.percentage
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        percentage = d.pop("percentage", UNSET)

        value = d.pop("value", UNSET)

        invoice_discount_position_model = cls(
            id=id,
            text=text,
            percentage=percentage,
            value=value,
        )

        invoice_discount_position_model.additional_properties = d
        return invoice_discount_position_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
