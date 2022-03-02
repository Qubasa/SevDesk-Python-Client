from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ContactModelTaxSet")


@attr.s(auto_attribs=True)
class ContactModelTaxSet:
    """Tax set which is used in every invoice of the contact.

    Attributes:
        id (int): Unique identifier of the tax set
        object_name (str): Model name, which is 'TaxSet'
    """

    id: int
    object_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "objectName": object_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_name = d.pop("objectName")

        contact_model_tax_set = cls(
            id=id,
            object_name=object_name,
        )

        contact_model_tax_set.additional_properties = d
        return contact_model_tax_set

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
