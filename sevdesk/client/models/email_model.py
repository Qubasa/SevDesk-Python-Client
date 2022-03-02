import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.email_model_object import EmailModelObject
from ..models.email_model_sev_client import EmailModelSevClient
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailModel")


@attr.s(auto_attribs=True)
class EmailModel:
    """Email model

    Attributes:
        from_ (str): The sender of the email
        to (str): The recipient of the email
        subject (str): The subject of the email
        id (Union[Unset, int]): The email id
        object_name (Union[Unset, str]): The email object name
        create (Union[Unset, datetime.datetime]): Date of mail creation
        update (Union[Unset, datetime.datetime]): Date of last mail update
        object_ (Union[Unset, None, EmailModelObject]): The contact used in the document
        text (Union[Unset, None, str]): The text of the email
        sev_client (Union[Unset, EmailModelSevClient]): Client to which mail belongs. Will be filled automatically
        cc (Union[Unset, None, str]): A list of mail addresses which are in the cc
        bcc (Union[Unset, None, str]): A list of mail addresses which are in the bcc
        arrived (Union[Unset, None, datetime.datetime]): Date the mail arrived
    """

    from_: str
    to: str
    subject: str
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    object_: Union[Unset, None, EmailModelObject] = UNSET
    text: Union[Unset, None, str] = UNSET
    sev_client: Union[Unset, EmailModelSevClient] = UNSET
    cc: Union[Unset, None, str] = UNSET
    bcc: Union[Unset, None, str] = UNSET
    arrived: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to
        subject = self.subject
        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        object_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict() if self.object_ else None

        text = self.text
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        cc = self.cc
        bcc = self.bcc
        arrived: Union[Unset, None, str] = UNSET
        if not isinstance(self.arrived, Unset):
            arrived = self.arrived.isoformat() if self.arrived else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "subject": subject,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if object_ is not UNSET:
            field_dict["object"] = object_
        if text is not UNSET:
            field_dict["text"] = text
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if arrived is not UNSET:
            field_dict["arrived"] = arrived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from")

        to = d.pop("to")

        subject = d.pop("subject")

        id = d.pop("id", UNSET)

        object_name = d.pop("objectName", UNSET)

        _create = d.pop("create", UNSET)
        create: Union[Unset, datetime.datetime]
        if isinstance(_create, Unset):
            create = UNSET
        else:
            create = isoparse(_create)

        _update = d.pop("update", UNSET)
        update: Union[Unset, datetime.datetime]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = isoparse(_update)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, None, EmailModelObject]
        if _object_ is None:
            object_ = None
        elif isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = EmailModelObject.from_dict(_object_)

        text = d.pop("text", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, EmailModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = EmailModelSevClient.from_dict(_sev_client)

        cc = d.pop("cc", UNSET)

        bcc = d.pop("bcc", UNSET)

        _arrived = d.pop("arrived", UNSET)
        arrived: Union[Unset, None, datetime.datetime]
        if _arrived is None:
            arrived = None
        elif isinstance(_arrived, Unset):
            arrived = UNSET
        else:
            arrived = isoparse(_arrived)

        email_model = cls(
            from_=from_,
            to=to,
            subject=subject,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            object_=object_,
            text=text,
            sev_client=sev_client,
            cc=cc,
            bcc=bcc,
            arrived=arrived,
        )

        email_model.additional_properties = d
        return email_model

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
