from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactAddAddressJsonBody")


@attr.s(auto_attribs=True)
class ContactAddAddressJsonBody:
    """
    Attributes:
        street (str): Street of the address.
        zip_ (str): Zip of the address
        city (str): City of the address
        country (Union[Unset, int]): ID of the country of the address Default: 1.
        category (Union[Unset, int]): ID of the category of the address Default: 43.
    """

    street: str
    zip_: str
    city: str
    country: Union[Unset, int] = 1
    category: Union[Unset, int] = 43
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        street = self.street
        zip_ = self.zip_
        city = self.city
        country = self.country
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "street": street,
                "zip": zip_,
                "city": city,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street = d.pop("street")

        zip_ = d.pop("zip")

        city = d.pop("city")

        country = d.pop("country", UNSET)

        category = d.pop("category", UNSET)

        contact_add_address_json_body = cls(
            street=street,
            zip_=zip_,
            city=city,
            country=country,
            category=category,
        )

        contact_add_address_json_body.additional_properties = d
        return contact_add_address_json_body

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
