from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber")


@attr.s(auto_attribs=True)
class GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber:
    """
    Attributes:
        id (Union[Unset, None, str]):
        number (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    number: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        number = d.pop("number", UNSET)

        get_accounting_types_response_200_objects_item_accounting_system_number = cls(
            id=id,
            number=number,
        )

        get_accounting_types_response_200_objects_item_accounting_system_number.additional_properties = (
            d
        )
        return get_accounting_types_response_200_objects_item_accounting_system_number

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
