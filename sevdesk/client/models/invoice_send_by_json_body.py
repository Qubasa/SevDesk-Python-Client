from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.invoice_send_by_json_body_send_type import InvoiceSendByJsonBodySendType

T = TypeVar("T", bound="InvoiceSendByJsonBody")


@attr.s(auto_attribs=True)
class InvoiceSendByJsonBody:
    """
    Attributes:
        send_type (InvoiceSendByJsonBodySendType): Specifies the way in which the document was sent to the customer.
            Accepts 'VPR' (print), 'VP' (postal), 'VM' (mail) and 'VPDF' (downloaded pfd).
        send_draft (bool): Specify if the should be enshrined after marking it as sent.
    """

    send_type: InvoiceSendByJsonBodySendType
    send_draft: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_type = self.send_type.value

        send_draft = self.send_draft

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sendType": send_type,
                "sendDraft": send_draft,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        send_type = InvoiceSendByJsonBodySendType(d.pop("sendType"))

        send_draft = d.pop("sendDraft")

        invoice_send_by_json_body = cls(
            send_type=send_type,
            send_draft=send_draft,
        )

        invoice_send_by_json_body.additional_properties = d
        return invoice_send_by_json_body

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
