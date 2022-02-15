from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.invoice_model import InvoiceModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelInvoiceResponse201")


@attr.s(auto_attribs=True)
class CancelInvoiceResponse201:
    """
    Attributes:
        objects (Union[Unset, List[InvoiceModel]]):
    """

    objects: Union[Unset, List[InvoiceModel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()

                objects.append(objects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        objects = []
        _objects = d.pop("objects", UNSET)
        for objects_item_data in _objects or []:
            objects_item = InvoiceModel.from_dict(objects_item_data)

            objects.append(objects_item)

        cancel_invoice_response_201 = cls(
            objects=objects,
        )

        cancel_invoice_response_201.additional_properties = d
        return cancel_invoice_response_201

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
