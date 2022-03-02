from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendInvoiceViaEMailJsonBody")


@attr.s(auto_attribs=True)
class SendInvoiceViaEMailJsonBody:
    """
    Attributes:
        to_email (str): The recipient of the email.
        subject (str): The subject of the email.
        text (str): The text of the email. Can contain html.
        copy (Union[Unset, bool]): Should a copy of this email be sent to you?
        additional_attachments (Union[Unset, str]): Additional attachments to the mail. String of IDs of existing
            documents in your sevdesk account separated by ','
        cc_email (Union[Unset, str]): String of mail addresses to be put as cc separated by ','
        bcc_email (Union[Unset, str]): String of mail addresses to be put as bcc separated by ','
    """

    to_email: str
    subject: str
    text: str
    copy: Union[Unset, bool] = UNSET
    additional_attachments: Union[Unset, str] = UNSET
    cc_email: Union[Unset, str] = UNSET
    bcc_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        to_email = self.to_email
        subject = self.subject
        text = self.text
        copy = self.copy
        additional_attachments = self.additional_attachments
        cc_email = self.cc_email
        bcc_email = self.bcc_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toEmail": to_email,
                "subject": subject,
                "text": text,
            }
        )
        if copy is not UNSET:
            field_dict["copy"] = copy
        if additional_attachments is not UNSET:
            field_dict["additionalAttachments"] = additional_attachments
        if cc_email is not UNSET:
            field_dict["ccEmail"] = cc_email
        if bcc_email is not UNSET:
            field_dict["bccEmail"] = bcc_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        to_email = d.pop("toEmail")

        subject = d.pop("subject")

        text = d.pop("text")

        copy = d.pop("copy", UNSET)

        additional_attachments = d.pop("additionalAttachments", UNSET)

        cc_email = d.pop("ccEmail", UNSET)

        bcc_email = d.pop("bccEmail", UNSET)

        send_invoice_via_e_mail_json_body = cls(
            to_email=to_email,
            subject=subject,
            text=text,
            copy=copy,
            additional_attachments=additional_attachments,
            cc_email=cc_email,
            bcc_email=bcc_email,
        )

        send_invoice_via_e_mail_json_body.additional_properties = d
        return send_invoice_via_e_mail_json_body

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
