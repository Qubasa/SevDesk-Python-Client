import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.accounting_contact_model_contact import AccountingContactModelContact
from ..models.accounting_contact_model_sev_client import AccountingContactModelSevClient
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountingContactModel")


@attr.s(auto_attribs=True)
class AccountingContactModel:
    """Accounting contact model

    Attributes:
        contact (AccountingContactModelContact): The contact to which this accounting contact belongs.
        id (Union[Unset, int]): The accounting contact id
        object_name (Union[Unset, str]): The accounting contact object name
        create (Union[Unset, datetime.datetime]): Date of accounting contact creation
        update (Union[Unset, datetime.datetime]): Date of last accounting contact update
        contact_name (Union[Unset, None, str]): Name of the contact to which this accounting contact belongs.
        sev_client (Union[Unset, AccountingContactModelSevClient]): Client to which accounting contact belongs. Will be
            filled automatically
        debitor_number (Union[Unset, None, int]): Debitor number of the accounting contact.
        creditor_number (Union[Unset, None, int]): Creditor number of the accounting contact.
    """

    contact: AccountingContactModelContact
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    contact_name: Union[Unset, None, str] = UNSET
    sev_client: Union[Unset, AccountingContactModelSevClient] = UNSET
    debitor_number: Union[Unset, None, int] = UNSET
    creditor_number: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact.to_dict()

        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        contact_name = self.contact_name
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        debitor_number = self.debitor_number
        creditor_number = self.creditor_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
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
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if debitor_number is not UNSET:
            field_dict["debitorNumber"] = debitor_number
        if creditor_number is not UNSET:
            field_dict["creditorNumber"] = creditor_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact = AccountingContactModelContact.from_dict(d.pop("contact"))

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

        contact_name = d.pop("contactName", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, AccountingContactModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = AccountingContactModelSevClient.from_dict(_sev_client)

        debitor_number = d.pop("debitorNumber", UNSET)

        creditor_number = d.pop("creditorNumber", UNSET)

        accounting_contact_model = cls(
            contact=contact,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            contact_name=contact_name,
            sev_client=sev_client,
            debitor_number=debitor_number,
            creditor_number=creditor_number,
        )

        accounting_contact_model.additional_properties = d
        return accounting_contact_model

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
