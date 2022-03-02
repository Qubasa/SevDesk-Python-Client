import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.communication_way_model import CommunicationWayModel
from ..models.contact_address import ContactAddress
from ..models.contact_model_category import ContactModelCategory
from ..models.contact_model_parent import ContactModelParent
from ..models.contact_model_sev_client import ContactModelSevClient
from ..models.contact_model_tax_set import ContactModelTaxSet
from ..models.contact_model_tax_type import ContactModelTaxType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactModel")


@attr.s(auto_attribs=True)
class ContactModel:
    """
    Attributes:
        category (ContactModelCategory): Category of the contact.<br> For more information, see <a
            href='https://my.sevdesk.de/apiOverview/index.html#/doc-contacts#types'>here</a>.
        addresses (Union[Unset, List[ContactAddress]]): Optional addresses added if embed contains addresses
        communication_ways (Union[Unset, List[CommunicationWayModel]]): Optional communication ways added if embed
            contains communicationWays
        id (Union[Unset, int]): The contact id
        object_name (Union[Unset, str]): The contact object name
        create (Union[Unset, datetime.datetime]): Date of contact creation
        update (Union[Unset, datetime.datetime]): Date of last contact update
        name (Union[Unset, None, str]): The organization name.<br>
            Be aware that the type of contact will depend on this attribute.<br>
            If it holds a value, the contact will be regarded as an organization.
        customer_number (Union[Unset, None, str]): The customer number Example: Customer-1337.
        parent (Union[Unset, None, ContactModelParent]): The parent contact to which this contact belongs. Must be an
            organization.
        surename (Union[Unset, None, str]): The first name of the contact. Yeah... not quite right in literally every
            way. We know. Not to be used for organizations. Example: John.
        familyname (Union[Unset, None, str]): The last name of the contact. Not to be used for organizations. Example:
            Snow.
        titel (Union[Unset, None, str]): A non-academic title for the contact. Not to be used for organizations.
            Example: Commander.
        description (Union[Unset, None, str]): A description for the contact. Example: Rightful king of the seven
            kingdoms.
        academic_title (Union[Unset, None, str]): A academic title for the contact. Not to be used for organizations.
        gender (Union[Unset, None, str]): Gender of the contact. Not to be used for organizations.
        sev_client (Union[Unset, ContactModelSevClient]): Client to which contact belongs. Will be filled automatically
        name2 (Union[Unset, None, str]): Second name of the contact. Not to be used for organizations. Example:
            Targaryen.
        birthday (Union[Unset, None, datetime.date]): Birthday of the contact. Not to be used for organizations.
        vat_number (Union[Unset, None, str]): Vat number of the contact.
        bank_account (Union[Unset, None, str]): Bank account number (IBAN) of the contact.
        bank_number (Union[Unset, None, str]): Bank number of the bank used by the contact.
        default_cashback_time (Union[Unset, None, int]): Absolute time in days which the contact has to pay his invoices
            and subsequently get a cashback.
        default_cashback_percent (Union[Unset, None, float]): Percentage of the invoice sum the contact gets back if he
            payed invoices in time.
        default_time_to_pay (Union[Unset, None, int]): The payment goal in days which is set for every invoice of the
            contact.
        tax_number (Union[Unset, None, str]): The tax number of the contact.
        tax_office (Union[Unset, None, str]): The tax office responsible for the contact.
        exempt_vat (Union[Unset, None, bool]): Defines if the contact is freed from paying vat.
        tax_type (Union[Unset, None, ContactModelTaxType]): Defines which tax regulation the contact is using.
        tax_set (Union[Unset, None, ContactModelTaxSet]): Tax set which is used in every invoice of the contact.
        default_discount_amount (Union[Unset, None, float]): The default discount the contact gets for every invoice.
            Depending on defaultDiscountPercentage attribute, in percent or absolute value.
        default_discount_percentage (Union[Unset, None, bool]): Defines if the discount is a percentage (true) or an
            absolute value (false).
    """

    category: ContactModelCategory
    addresses: Union[Unset, List[ContactAddress]] = UNSET
    communication_ways: Union[Unset, List[CommunicationWayModel]] = UNSET
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, None, str] = UNSET
    customer_number: Union[Unset, None, str] = UNSET
    parent: Union[Unset, None, ContactModelParent] = UNSET
    surename: Union[Unset, None, str] = UNSET
    familyname: Union[Unset, None, str] = UNSET
    titel: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    academic_title: Union[Unset, None, str] = UNSET
    gender: Union[Unset, None, str] = UNSET
    sev_client: Union[Unset, ContactModelSevClient] = UNSET
    name2: Union[Unset, None, str] = UNSET
    birthday: Union[Unset, None, datetime.date] = UNSET
    vat_number: Union[Unset, None, str] = UNSET
    bank_account: Union[Unset, None, str] = UNSET
    bank_number: Union[Unset, None, str] = UNSET
    default_cashback_time: Union[Unset, None, int] = UNSET
    default_cashback_percent: Union[Unset, None, float] = UNSET
    default_time_to_pay: Union[Unset, None, int] = UNSET
    tax_number: Union[Unset, None, str] = UNSET
    tax_office: Union[Unset, None, str] = UNSET
    exempt_vat: Union[Unset, None, bool] = UNSET
    tax_type: Union[Unset, None, ContactModelTaxType] = UNSET
    tax_set: Union[Unset, None, ContactModelTaxSet] = UNSET
    default_discount_amount: Union[Unset, None, float] = UNSET
    default_discount_percentage: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.to_dict()

        addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()

                addresses.append(addresses_item)

        communication_ways: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.communication_ways, Unset):
            communication_ways = []
            for communication_ways_item_data in self.communication_ways:
                communication_ways_item = communication_ways_item_data.to_dict()

                communication_ways.append(communication_ways_item)

        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        name = self.name
        customer_number = self.customer_number
        parent: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict() if self.parent else None

        surename = self.surename
        familyname = self.familyname
        titel = self.titel
        description = self.description
        academic_title = self.academic_title
        gender = self.gender
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        name2 = self.name2
        birthday: Union[Unset, None, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat() if self.birthday else None

        vat_number = self.vat_number
        bank_account = self.bank_account
        bank_number = self.bank_number
        default_cashback_time = self.default_cashback_time
        default_cashback_percent = self.default_cashback_percent
        default_time_to_pay = self.default_time_to_pay
        tax_number = self.tax_number
        tax_office = self.tax_office
        exempt_vat = self.exempt_vat
        tax_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.tax_type, Unset):
            tax_type = self.tax_type.value if self.tax_type else None

        tax_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_set, Unset):
            tax_set = self.tax_set.to_dict() if self.tax_set else None

        default_discount_amount = self.default_discount_amount
        default_discount_percentage = self.default_discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if communication_ways is not UNSET:
            field_dict["communicationWays"] = communication_ways
        if id is not UNSET:
            field_dict["id"] = id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if name is not UNSET:
            field_dict["name"] = name
        if customer_number is not UNSET:
            field_dict["customerNumber"] = customer_number
        if parent is not UNSET:
            field_dict["parent"] = parent
        if surename is not UNSET:
            field_dict["surename"] = surename
        if familyname is not UNSET:
            field_dict["familyname"] = familyname
        if titel is not UNSET:
            field_dict["titel"] = titel
        if description is not UNSET:
            field_dict["description"] = description
        if academic_title is not UNSET:
            field_dict["academicTitle"] = academic_title
        if gender is not UNSET:
            field_dict["gender"] = gender
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if name2 is not UNSET:
            field_dict["name2"] = name2
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number
        if bank_account is not UNSET:
            field_dict["bankAccount"] = bank_account
        if bank_number is not UNSET:
            field_dict["bankNumber"] = bank_number
        if default_cashback_time is not UNSET:
            field_dict["defaultCashbackTime"] = default_cashback_time
        if default_cashback_percent is not UNSET:
            field_dict["defaultCashbackPercent"] = default_cashback_percent
        if default_time_to_pay is not UNSET:
            field_dict["defaultTimeToPay"] = default_time_to_pay
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if tax_office is not UNSET:
            field_dict["taxOffice"] = tax_office
        if exempt_vat is not UNSET:
            field_dict["exemptVat"] = exempt_vat
        if tax_type is not UNSET:
            field_dict["taxType"] = tax_type
        if tax_set is not UNSET:
            field_dict["taxSet"] = tax_set
        if default_discount_amount is not UNSET:
            field_dict["defaultDiscountAmount"] = default_discount_amount
        if default_discount_percentage is not UNSET:
            field_dict["defaultDiscountPercentage"] = default_discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = ContactModelCategory.from_dict(d.pop("category"))

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = ContactAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        communication_ways = []
        _communication_ways = d.pop("communicationWays", UNSET)
        for communication_ways_item_data in _communication_ways or []:
            communication_ways_item = CommunicationWayModel.from_dict(
                communication_ways_item_data
            )

            communication_ways.append(communication_ways_item)

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

        name = d.pop("name", UNSET)

        customer_number = d.pop("customerNumber", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, None, ContactModelParent]
        if _parent is None:
            parent = None
        elif isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ContactModelParent.from_dict(_parent)

        surename = d.pop("surename", UNSET)

        familyname = d.pop("familyname", UNSET)

        titel = d.pop("titel", UNSET)

        description = d.pop("description", UNSET)

        academic_title = d.pop("academicTitle", UNSET)

        gender = d.pop("gender", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, ContactModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = ContactModelSevClient.from_dict(_sev_client)

        name2 = d.pop("name2", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, None, datetime.date]
        if _birthday is None:
            birthday = None
        elif isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = isoparse(_birthday).date()

        vat_number = d.pop("vatNumber", UNSET)

        bank_account = d.pop("bankAccount", UNSET)

        bank_number = d.pop("bankNumber", UNSET)

        default_cashback_time = d.pop("defaultCashbackTime", UNSET)

        default_cashback_percent = d.pop("defaultCashbackPercent", UNSET)

        default_time_to_pay = d.pop("defaultTimeToPay", UNSET)

        tax_number = d.pop("taxNumber", UNSET)

        tax_office = d.pop("taxOffice", UNSET)

        exempt_vat = d.pop("exemptVat", UNSET)

        _tax_type = d.pop("taxType", UNSET)
        tax_type: Union[Unset, None, ContactModelTaxType]
        if _tax_type is None:
            tax_type = None
        elif isinstance(_tax_type, Unset):
            tax_type = UNSET
        else:
            tax_type = ContactModelTaxType(_tax_type)

        _tax_set = d.pop("taxSet", UNSET)
        tax_set: Union[Unset, None, ContactModelTaxSet]
        if _tax_set is None:
            tax_set = None
        elif isinstance(_tax_set, Unset):
            tax_set = UNSET
        else:
            tax_set = ContactModelTaxSet.from_dict(_tax_set)

        default_discount_amount = d.pop("defaultDiscountAmount", UNSET)

        default_discount_percentage = d.pop("defaultDiscountPercentage", UNSET)

        contact_model = cls(
            category=category,
            addresses=addresses,
            communication_ways=communication_ways,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            name=name,
            customer_number=customer_number,
            parent=parent,
            surename=surename,
            familyname=familyname,
            titel=titel,
            description=description,
            academic_title=academic_title,
            gender=gender,
            sev_client=sev_client,
            name2=name2,
            birthday=birthday,
            vat_number=vat_number,
            bank_account=bank_account,
            bank_number=bank_number,
            default_cashback_time=default_cashback_time,
            default_cashback_percent=default_cashback_percent,
            default_time_to_pay=default_time_to_pay,
            tax_number=tax_number,
            tax_office=tax_office,
            exempt_vat=exempt_vat,
            tax_type=tax_type,
            tax_set=tax_set,
            default_discount_amount=default_discount_amount,
            default_discount_percentage=default_discount_percentage,
        )

        contact_model.additional_properties = d
        return contact_model

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
