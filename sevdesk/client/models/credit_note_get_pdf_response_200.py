from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credit_note_get_pdf_response_200_objects import (
    CreditNoteGetPdfResponse200Objects,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditNoteGetPdfResponse200")


@attr.s(auto_attribs=True)
class CreditNoteGetPdfResponse200:
    """
    Attributes:
        objects (Union[Unset, CreditNoteGetPdfResponse200Objects]):
    """

    objects: Union[Unset, CreditNoteGetPdfResponse200Objects] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = self.objects.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _objects = d.pop("objects", UNSET)
        objects: Union[Unset, CreditNoteGetPdfResponse200Objects]
        if isinstance(_objects, Unset):
            objects = UNSET
        else:
            objects = CreditNoteGetPdfResponse200Objects.from_dict(_objects)

        credit_note_get_pdf_response_200 = cls(
            objects=objects,
        )

        credit_note_get_pdf_response_200.additional_properties = d
        return credit_note_get_pdf_response_200

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
