from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_note import CreditNote


T = TypeVar("T", bound="CreditNoteChangeStatusResponse200")


@attr.s(auto_attribs=True)
class CreditNoteChangeStatusResponse200:
    """
    Attributes:
        objects (Union[Unset, CreditNote]):
    """

    objects: Union[Unset, "CreditNote"] = UNSET
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
        from ..models.credit_note import CreditNote

        d = src_dict.copy()
        _objects = d.pop("objects", UNSET)
        objects: Union[Unset, CreditNote]
        if isinstance(_objects, Unset):
            objects = UNSET
        else:
            objects = CreditNote.from_dict(_objects)

        credit_note_change_status_response_200 = cls(
            objects=objects,
        )

        credit_note_change_status_response_200.additional_properties = d
        return credit_note_change_status_response_200

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
