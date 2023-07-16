from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationErrorError")


@attr.s(auto_attribs=True)
class ValidationErrorError:
    """
    Attributes:
        message (Union[Unset, str]):
        exception_uuid (Union[Unset, str]): An identifier of this exact problem that can be given to the support team.
    """

    message: Union[Unset, str] = UNSET
    exception_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        exception_uuid = self.exception_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if exception_uuid is not UNSET:
            field_dict["exceptionUUID"] = exception_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        exception_uuid = d.pop("exceptionUUID", UNSET)

        validation_error_error = cls(
            message=message,
            exception_uuid=exception_uuid,
        )

        validation_error_error.additional_properties = d
        return validation_error_error

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
