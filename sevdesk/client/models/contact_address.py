import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_address_category import ContactAddressCategory
    from ..models.contact_address_contact import ContactAddressContact
    from ..models.contact_address_country import ContactAddressCountry
    from ..models.contact_address_sev_client import ContactAddressSevClient


T = TypeVar("T", bound="ContactAddress")


@attr.s(auto_attribs=True)
class ContactAddress:
    """ContactAddress model

    Attributes:
        contact (ContactAddressContact): The contact to which this contact address belongs.
        country (ContactAddressCountry):
        id (Union[Unset, int]): The contact address id
        object_name (Union[Unset, str]): The contact address object name
        create (Union[Unset, datetime.datetime]): Date of contact address creation
        update (Union[Unset, datetime.datetime]): Date of last contact address update
        street (Union[Unset, None, str]): Street name Example: South road 15.
        zip_ (Union[Unset, None, str]): Zib code Example: 12345.
        city (Union[Unset, None, str]): City name Example: The North.
        category (Union[Unset, None, ContactAddressCategory]): Category of the contact address. For all categories, send
            a GET to /Category?objectType=ContactAddress.
        name (Union[Unset, None, str]): Name in address Example: John Snow.
        sev_client (Union[Unset, ContactAddressSevClient]): Client to which contact address belongs. Will be filled
            automatically
        name2 (Union[Unset, str]): Second name in address Example: Targaryen.
        name3 (Union[Unset, None, str]): Third name in address
        name4 (Union[Unset, None, str]): Fourth name in address
    """

    contact: "ContactAddressContact"
    country: "ContactAddressCountry"
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    street: Union[Unset, None, str] = UNSET
    zip_: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, "ContactAddressCategory"] = UNSET
    name: Union[Unset, None, str] = UNSET
    sev_client: Union[Unset, "ContactAddressSevClient"] = UNSET
    name2: Union[Unset, str] = UNSET
    name3: Union[Unset, None, str] = UNSET
    name4: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact.to_dict()

        country = self.country.to_dict()

        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        street = self.street
        zip_ = self.zip_
        city = self.city
        category: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict() if self.category else None

        name = self.name
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        name2 = self.name2
        name3 = self.name3
        name4 = self.name4

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "country": country,
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
        if street is not UNSET:
            field_dict["street"] = street
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if city is not UNSET:
            field_dict["city"] = city
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if name2 is not UNSET:
            field_dict["name2"] = name2
        if name3 is not UNSET:
            field_dict["name3"] = name3
        if name4 is not UNSET:
            field_dict["name4"] = name4

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_address_category import ContactAddressCategory
        from ..models.contact_address_contact import ContactAddressContact
        from ..models.contact_address_country import ContactAddressCountry
        from ..models.contact_address_sev_client import ContactAddressSevClient

        d = src_dict.copy()
        contact = ContactAddressContact.from_dict(d.pop("contact"))

        country = ContactAddressCountry.from_dict(d.pop("country"))

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

        street = d.pop("street", UNSET)

        zip_ = d.pop("zip", UNSET)

        city = d.pop("city", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, None, ContactAddressCategory]
        if _category is None:
            category = None
        elif isinstance(_category, Unset):
            category = UNSET
        else:
            category = ContactAddressCategory.from_dict(_category)

        name = d.pop("name", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, ContactAddressSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = ContactAddressSevClient.from_dict(_sev_client)

        name2 = d.pop("name2", UNSET)

        name3 = d.pop("name3", UNSET)

        name4 = d.pop("name4", UNSET)

        contact_address = cls(
            contact=contact,
            country=country,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            street=street,
            zip_=zip_,
            city=city,
            category=category,
            name=name,
            sev_client=sev_client,
            name2=name2,
            name3=name3,
            name4=name4,
        )

        contact_address.additional_properties = d
        return contact_address

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
