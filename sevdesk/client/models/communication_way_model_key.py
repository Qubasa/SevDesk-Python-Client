from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CommunicationWayModelKey")


@attr.s(auto_attribs=True)
class CommunicationWayModelKey:
    """The key of the communication way. Similar to the category of addresses. For all communication way keys please send a
    GET to /CommunicationWayKey.

        Attributes:
            id (int): Unique identifier of the key
            object_name (str): Model name, which is 'CommunicationWayKey' Default: 'CommunicationWayKey'. Example:
                CommunicationWayKey.
    """

    id: int
    object_name: str = "CommunicationWayKey"
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

        communication_way_model_key = cls(
            id=id,
            object_name=object_name,
        )

        communication_way_model_key.additional_properties = d
        return communication_way_model_key

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
