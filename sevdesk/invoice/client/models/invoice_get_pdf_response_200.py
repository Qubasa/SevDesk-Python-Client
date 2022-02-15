from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="InvoiceGetPdfResponse200")


@attr.s(auto_attribs=True)
class InvoiceGetPdfResponse200:
    """
    Attributes:
        filename (Union[Unset, str]):
        mime_type (Union[Unset, str]):
        content (Union[Unset, File]):
        base64encoded (Union[Unset, str]):
    """

    filename: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    content: Union[Unset, File] = UNSET
    base64encoded: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filename = self.filename
        mime_type = self.mime_type
        content: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_tuple()

        base64encoded = self.base64encoded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if content is not UNSET:
            field_dict["content"] = content
        if base64encoded is not UNSET:
            field_dict["base64encoded"] = base64encoded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filename = d.pop("filename", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        _content = d.pop("content", UNSET)
        content: Union[Unset, File]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = File(payload=BytesIO(_content))

        base64encoded = d.pop("base64encoded", UNSET)

        invoice_get_pdf_response_200 = cls(
            filename=filename,
            mime_type=mime_type,
            content=content,
            base64encoded=base64encoded,
        )

        invoice_get_pdf_response_200.additional_properties = d
        return invoice_get_pdf_response_200

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
