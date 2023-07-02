from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_accounting_types_response_200_objects_item_accounting_system_number import (
        GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber,
    )
    from ..models.get_accounting_types_response_200_objects_item_parent import (
        GetAccountingTypesResponse200ObjectsItemParent,
    )


T = TypeVar("T", bound="GetAccountingTypesResponse200ObjectsItem")


@attr.s(auto_attribs=True)
class GetAccountingTypesResponse200ObjectsItem:
    """
    Attributes:
        id (Union[Unset, None, str]):
        object_name (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        skr03 (Union[Unset, None, str]):
        skr04 (Union[Unset, None, str]):
        skr_at (Union[Unset, None, str]):
        skr_ch (Union[Unset, None, str]):
        skr_gr (Union[Unset, None, str]):
        translation_code (Union[Unset, None, str]):
        parent (Union[Unset, None, GetAccountingTypesResponse200ObjectsItemParent]):
        accounting_system_number (Union[Unset, None, GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber]):
    """

    id: Union[Unset, None, str] = UNSET
    object_name: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    skr03: Union[Unset, None, str] = UNSET
    skr04: Union[Unset, None, str] = UNSET
    skr_at: Union[Unset, None, str] = UNSET
    skr_ch: Union[Unset, None, str] = UNSET
    skr_gr: Union[Unset, None, str] = UNSET
    translation_code: Union[Unset, None, str] = UNSET
    parent: Union[Unset, None, "GetAccountingTypesResponse200ObjectsItemParent"] = UNSET
    accounting_system_number: Union[
        Unset, None, "GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name
        name = self.name
        skr03 = self.skr03
        skr04 = self.skr04
        skr_at = self.skr_at
        skr_ch = self.skr_ch
        skr_gr = self.skr_gr
        translation_code = self.translation_code
        parent: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict() if self.parent else None

        accounting_system_number: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.accounting_system_number, Unset):
            accounting_system_number = (
                self.accounting_system_number.to_dict()
                if self.accounting_system_number
                else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if name is not UNSET:
            field_dict["name"] = name
        if skr03 is not UNSET:
            field_dict["skr03"] = skr03
        if skr04 is not UNSET:
            field_dict["skr04"] = skr04
        if skr_at is not UNSET:
            field_dict["skrAt"] = skr_at
        if skr_ch is not UNSET:
            field_dict["skrCh"] = skr_ch
        if skr_gr is not UNSET:
            field_dict["skrGr"] = skr_gr
        if translation_code is not UNSET:
            field_dict["translationCode"] = translation_code
        if parent is not UNSET:
            field_dict["parent"] = parent
        if accounting_system_number is not UNSET:
            field_dict["accountingSystemNumber"] = accounting_system_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_accounting_types_response_200_objects_item_accounting_system_number import (
            GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber,
        )
        from ..models.get_accounting_types_response_200_objects_item_parent import (
            GetAccountingTypesResponse200ObjectsItemParent,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        object_name = d.pop("objectName", UNSET)

        name = d.pop("name", UNSET)

        skr03 = d.pop("skr03", UNSET)

        skr04 = d.pop("skr04", UNSET)

        skr_at = d.pop("skrAt", UNSET)

        skr_ch = d.pop("skrCh", UNSET)

        skr_gr = d.pop("skrGr", UNSET)

        translation_code = d.pop("translationCode", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, None, GetAccountingTypesResponse200ObjectsItemParent]
        if _parent is None:
            parent = None
        elif isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = GetAccountingTypesResponse200ObjectsItemParent.from_dict(_parent)

        _accounting_system_number = d.pop("accountingSystemNumber", UNSET)
        accounting_system_number: Union[
            Unset, None, GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber
        ]
        if _accounting_system_number is None:
            accounting_system_number = None
        elif isinstance(_accounting_system_number, Unset):
            accounting_system_number = UNSET
        else:
            accounting_system_number = GetAccountingTypesResponse200ObjectsItemAccountingSystemNumber.from_dict(
                _accounting_system_number
            )

        get_accounting_types_response_200_objects_item = cls(
            id=id,
            object_name=object_name,
            name=name,
            skr03=skr03,
            skr04=skr04,
            skr_at=skr_at,
            skr_ch=skr_ch,
            skr_gr=skr_gr,
            translation_code=translation_code,
            parent=parent,
            accounting_system_number=accounting_system_number,
        )

        get_accounting_types_response_200_objects_item.additional_properties = d
        return get_accounting_types_response_200_objects_item

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
