from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VoucherResponseModelSupplier")


@attr.s(auto_attribs=True)
class VoucherResponseModelSupplier:
    """The contact used in the voucher as a supplier.<br>
    If you don't have a contact as a supplier, you can set this object to null.

        Attributes:
            id (int): Unique identifier of the contact
            object_name (str): Model name, which is 'Contact' Example: Contact.
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

        voucher_response_model_supplier = cls(
            id=id,
            object_name=object_name,
        )

        voucher_response_model_supplier.additional_properties = d
        return voucher_response_model_supplier

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
