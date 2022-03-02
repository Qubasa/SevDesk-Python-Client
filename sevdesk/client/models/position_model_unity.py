from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionModelUnity")


@attr.s(auto_attribs=True)
class PositionModelUnity:
    """The unit in which the positions part is measured

    Attributes:
        id (int): Unique identifier of the unit Example: 1.
        object_name (str): Model name, which is 'Unity' Default: 'Unity'.
        translation_code (Union[Unset, str]): Translation Code
    """

    id: int
    object_name: str = "Unity"
    translation_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name
        translation_code = self.translation_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "objectName": object_name,
            }
        )
        if translation_code is not UNSET:
            field_dict["translationCode"] = translation_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_name = d.pop("objectName")

        translation_code = d.pop("translationCode", UNSET)

        position_model_unity = cls(
            id=id,
            object_name=object_name,
            translation_code=translation_code,
        )

        position_model_unity.additional_properties = d
        return position_model_unity

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
