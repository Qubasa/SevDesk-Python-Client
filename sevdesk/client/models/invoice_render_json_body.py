from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceRenderJsonBody")


@attr.s(auto_attribs=True)
class InvoiceRenderJsonBody:
    """
    Attributes:
        draft (Union[Unset, bool]):
        force_reload (Union[Unset, bool]): Define if a forceful re-render should occur.
    """

    draft: Union[Unset, bool] = UNSET
    force_reload: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        draft = self.draft
        force_reload = self.force_reload

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft
        if force_reload is not UNSET:
            field_dict["forceReload"] = force_reload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        draft = d.pop("draft", UNSET)

        force_reload = d.pop("forceReload", UNSET)

        invoice_render_json_body = cls(
            draft=draft,
            force_reload=force_reload,
        )

        invoice_render_json_body.additional_properties = d
        return invoice_render_json_body

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
