from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.invoice_change_status_json_body_value import (
    InvoiceChangeStatusJsonBodyValue,
)

T = TypeVar("T", bound="InvoiceChangeStatusJsonBody")


@attr.s(auto_attribs=True)
class InvoiceChangeStatusJsonBody:
    """
    Attributes:
        value (InvoiceChangeStatusJsonBodyValue): Please have a look in our
                 <a href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-invoices#types'>API-Overview</a>
                 to see what the different status codes mean Example: 100.
    """

    value: InvoiceChangeStatusJsonBodyValue
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = InvoiceChangeStatusJsonBodyValue(d.pop("value"))

        invoice_change_status_json_body = cls(
            value=value,
        )

        invoice_change_status_json_body.additional_properties = d
        return invoice_change_status_json_body

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
