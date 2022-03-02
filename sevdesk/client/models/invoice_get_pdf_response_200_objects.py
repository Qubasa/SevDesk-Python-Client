from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceGetPdfResponse200Objects")


@attr.s(auto_attribs=True)
class InvoiceGetPdfResponse200Objects:
    """
    Attributes:
        filename (Union[Unset, str]):
        mimetype (Union[Unset, str]):
        content (Union[Unset, str]):
        base_64_encoded (Union[Unset, bool]):
    """

    filename: Union[Unset, str] = UNSET
    mimetype: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    base_64_encoded: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filename = self.filename
        mimetype = self.mimetype
        content = self.content
        base_64_encoded = self.base_64_encoded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if content is not UNSET:
            field_dict["content"] = content
        if base_64_encoded is not UNSET:
            field_dict["base64Encoded"] = base_64_encoded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filename = d.pop("filename", UNSET)

        mimetype = d.pop("mimetype", UNSET)

        content = d.pop("content", UNSET)

        base_64_encoded = d.pop("base64Encoded", UNSET)

        invoice_get_pdf_response_200_objects = cls(
            filename=filename,
            mimetype=mimetype,
            content=content,
            base_64_encoded=base_64_encoded,
        )

        invoice_get_pdf_response_200_objects.additional_properties = d
        return invoice_get_pdf_response_200_objects

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
