import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.communication_way_model_contact import CommunicationWayModelContact
from ..models.communication_way_model_key import CommunicationWayModelKey
from ..models.communication_way_model_sev_client import CommunicationWayModelSevClient
from ..models.communication_way_model_type import CommunicationWayModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationWayModel")


@attr.s(auto_attribs=True)
class CommunicationWayModel:
    """Contact communication way model

    Attributes:
        type (CommunicationWayModelType): Type of the communication way Example: EMAIL.
        value (str): The value of the communication way.<br>
                 For example the phone number, e-mail address or website.
        key (CommunicationWayModelKey): The key of the communication way.<br>
            Similar to the category of addresses.<br>
            For all communication way keys please send a GET to /CommunicationWayKey.
        id (Union[Unset, int]): The communication way id
        object_name (Union[Unset, str]): The communication way object name
        create (Union[Unset, datetime.datetime]): Date of communication way creation
        update (Union[Unset, datetime.datetime]): Date of last communication way update
        contact (Union[Unset, CommunicationWayModelContact]): The contact to which this communication way belongs.
        main (Union[Unset, None, bool]): Defines whether the communication way is the main communication way for the
            contact.
        sev_client (Union[Unset, CommunicationWayModelSevClient]): Client to which communication way key belongs. Will
            be filled automatically
    """

    type: CommunicationWayModelType
    value: str
    key: CommunicationWayModelKey
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    contact: Union[Unset, CommunicationWayModelContact] = UNSET
    main: Union[Unset, None, bool] = UNSET
    sev_client: Union[Unset, CommunicationWayModelSevClient] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value
        key = self.key.to_dict()

        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        main = self.main
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "value": value,
                "key": key,
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
        if contact is not UNSET:
            field_dict["contact"] = contact
        if main is not UNSET:
            field_dict["main"] = main
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CommunicationWayModelType(d.pop("type"))

        value = d.pop("value")

        key = CommunicationWayModelKey.from_dict(d.pop("key"))

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

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, CommunicationWayModelContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = CommunicationWayModelContact.from_dict(_contact)

        main = d.pop("main", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, CommunicationWayModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = CommunicationWayModelSevClient.from_dict(_sev_client)

        communication_way_model = cls(
            type=type,
            value=value,
            key=key,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            contact=contact,
            main=main,
            sev_client=sev_client,
        )

        communication_way_model.additional_properties = d
        return communication_way_model

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
