from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveInvoiceDiscountSave")


@attr.s(auto_attribs=True)
class SaveInvoiceDiscountSave:
    """
    Attributes:
        discount (bool): Defines if this is a discount or a surcharge Example: true.
        text (str): A text for your discount
        percentage (bool): Defines if this is a percentage or an absolute discount
        value (float): Value of the discount
        object_name (str): Object name of the discount Default: 'Discounts'.
        map_all (bool): Internal param Default: True.
        id (Union[Unset, None, int]): The invoice position id
    """

    discount: bool
    text: str
    percentage: bool
    value: float
    object_name: str = "Discounts"
    map_all: bool = True
    id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discount = self.discount
        text = self.text
        percentage = self.percentage
        value = self.value
        object_name = self.object_name
        map_all = self.map_all
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discount": discount,
                "text": text,
                "percentage": percentage,
                "value": value,
                "objectName": object_name,
                "mapAll": map_all,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        discount = d.pop("discount")

        text = d.pop("text")

        percentage = d.pop("percentage")

        value = d.pop("value")

        object_name = d.pop("objectName")

        map_all = d.pop("mapAll")

        id = d.pop("id", UNSET)

        save_invoice_discount_save = cls(
            discount=discount,
            text=text,
            percentage=percentage,
            value=value,
            object_name=object_name,
            map_all=map_all,
            id=id,
        )

        save_invoice_discount_save.additional_properties = d
        return save_invoice_discount_save

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
