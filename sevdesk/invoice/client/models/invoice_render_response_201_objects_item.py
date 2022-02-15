from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceRenderResponse201ObjectsItem")


@attr.s(auto_attribs=True)
class InvoiceRenderResponse201ObjectsItem:
    """
    Attributes:
        doc_id (Union[Unset, str]): ID of the (temporary) document.
        pdf_url (Union[Unset, str]): The url location of the (temporary) document.
        pages (Union[Unset, int]): The amount of pages of the document.
    """

    doc_id: Union[Unset, str] = UNSET
    pdf_url: Union[Unset, str] = UNSET
    pages: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_id = self.doc_id
        pdf_url = self.pdf_url
        pages = self.pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if pdf_url is not UNSET:
            field_dict["pdfUrl"] = pdf_url
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_id = d.pop("docId", UNSET)

        pdf_url = d.pop("pdfUrl", UNSET)

        pages = d.pop("pages", UNSET)

        invoice_render_response_201_objects_item = cls(
            doc_id=doc_id,
            pdf_url=pdf_url,
            pages=pages,
        )

        invoice_render_response_201_objects_item.additional_properties = d
        return invoice_render_response_201_objects_item

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
