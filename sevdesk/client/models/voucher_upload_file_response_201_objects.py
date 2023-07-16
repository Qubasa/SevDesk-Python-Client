from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherUploadFileResponse201Objects")


@attr.s(auto_attribs=True)
class VoucherUploadFileResponse201Objects:
    """
    Attributes:
        pages (Union[Unset, float]):  Example: 1.
        mime_type (Union[Unset, str]):  Example: image/jpg.
        origin_mime_type (Union[Unset, str]):  Example: application/pdf.
        filename (Union[Unset, str]):  Example: f019bec36c65f5a0e7d2c63cc33f0681.pdf.
        content_hash (Union[Unset, str]):  Example: 1998dea8c6e9e489139caf896690641c0ea065ce5770b51cf2a4d10797f99685.
        content (Union[Unset, List[Any]]):
    """

    pages: Union[Unset, float] = UNSET
    mime_type: Union[Unset, str] = UNSET
    origin_mime_type: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    content_hash: Union[Unset, str] = UNSET
    content: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pages = self.pages
        mime_type = self.mime_type
        origin_mime_type = self.origin_mime_type
        filename = self.filename
        content_hash = self.content_hash
        content: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pages is not UNSET:
            field_dict["pages"] = pages
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if origin_mime_type is not UNSET:
            field_dict["originMimeType"] = origin_mime_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pages = d.pop("pages", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        origin_mime_type = d.pop("originMimeType", UNSET)

        filename = d.pop("filename", UNSET)

        content_hash = d.pop("contentHash", UNSET)

        content = cast(List[Any], d.pop("content", UNSET))

        voucher_upload_file_response_201_objects = cls(
            pages=pages,
            mime_type=mime_type,
            origin_mime_type=origin_mime_type,
            filename=filename,
            content_hash=content_hash,
            content=content,
        )

        voucher_upload_file_response_201_objects.additional_properties = d
        return voucher_upload_file_response_201_objects

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
