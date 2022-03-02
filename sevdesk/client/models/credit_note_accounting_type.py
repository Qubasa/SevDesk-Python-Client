from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditNoteAccountingType")


@attr.s(auto_attribs=True)
class CreditNoteAccountingType:
    """The account on which this credit note should be booked - for booking category ACCOUNTING_TYPE

    Attributes:
        id (Union[Unset, int]): Unique identifier of the credit-note
        object_name (Union[Unset, str]): Model name, which is 'CreditNote' Default: 'AccountingType'.
    """

    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = "AccountingType"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        object_name = d.pop("objectName", UNSET)

        credit_note_accounting_type = cls(
            id=id,
            object_name=object_name,
        )

        credit_note_accounting_type.additional_properties = d
        return credit_note_accounting_type

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
