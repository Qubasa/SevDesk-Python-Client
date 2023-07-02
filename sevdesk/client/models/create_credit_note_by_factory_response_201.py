from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_credit_note_by_factory_response_201_objects import (
        CreateCreditNoteByFactoryResponse201Objects,
    )


T = TypeVar("T", bound="CreateCreditNoteByFactoryResponse201")


@attr.s(auto_attribs=True)
class CreateCreditNoteByFactoryResponse201:
    """
    Attributes:
        objects (Union[Unset, CreateCreditNoteByFactoryResponse201Objects]):
    """

    objects: Union[Unset, "CreateCreditNoteByFactoryResponse201Objects"] = UNSET
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
        from ..models.create_credit_note_by_factory_response_201_objects import (
            CreateCreditNoteByFactoryResponse201Objects,
        )

        d = src_dict.copy()
        _objects = d.pop("objects", UNSET)
        objects: Union[Unset, CreateCreditNoteByFactoryResponse201Objects]
        if isinstance(_objects, Unset):
            objects = UNSET
        else:
            objects = CreateCreditNoteByFactoryResponse201Objects.from_dict(_objects)

        create_credit_note_by_factory_response_201 = cls(
            objects=objects,
        )

        create_credit_note_by_factory_response_201.additional_properties = d
        return create_credit_note_by_factory_response_201

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
