from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactAddEmailJsonBody")


@attr.s(auto_attribs=True)
class ContactAddEmailJsonBody:
    """
    Attributes:
        key (int): ID of communication way key for the email which is added.
        value (str): Value of the email address.
        main (Union[Unset, bool]): Defines if the email is the main email of the contact.
    """

    key: int
    value: str
    main: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        value = self.value
        main = self.main

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if main is not UNSET:
            field_dict["main"] = main

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        value = d.pop("value")

        main = d.pop("main", UNSET)

        contact_add_email_json_body = cls(
            key=key,
            value=value,
            main=main,
        )

        contact_add_email_json_body.additional_properties = d
        return contact_add_email_json_body

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
