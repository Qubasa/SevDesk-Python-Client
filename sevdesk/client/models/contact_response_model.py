import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.contact_response_model_tax_type import ContactResponseModelTaxType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_response_model_category import ContactResponseModelCategory
    from ..models.contact_response_model_parent import ContactResponseModelParent
    from ..models.contact_response_model_sev_client import ContactResponseModelSevClient
    from ..models.contact_response_model_tax_set import ContactResponseModelTaxSet


T = TypeVar("T", bound="ContactResponseModel")


@attr.s(auto_attribs=True)
class ContactResponseModel:
    """Contact model

    Attributes:
        id (Union[Unset, str]): The contact id Example: 0.
        object_name (Union[Unset, str]): The contact object name Example: Contact.
        create (Union[Unset, datetime.datetime]): Date of contact creation
        update (Union[Unset, datetime.datetime]): Date of last contact update
        name (Union[Unset, str]): The organization name.<br>
            Be aware that the type of contact will depend on this attribute.<br>
            If it holds a value, the contact will be regarded as an organization. Example: string.
        status (Union[Unset, str]): Defines the status of the contact. 100 <-> Lead - 500 <-> Pending - 1000 <-> Active.
            Example: 100.
        customer_number (Union[Unset, str]): The customer number Example: Customer-1337.
        parent (Union[Unset, ContactResponseModelParent]): The parent contact to which this contact belongs. Must be an
            organization.
        surename (Union[Unset, str]): The <b>first</b> name of the contact.<br>
            Yeah... not quite right in literally every way. We know.<br>
            Not to be used for organizations. Example: John.
        familyname (Union[Unset, str]): The last name of the contact.<br>
            Not to be used for organizations. Example: Snow.
        titel (Union[Unset, str]): A non-academic title for the contact.
            Not to be used for organizations. Example: Commander.
        category (Union[Unset, ContactResponseModelCategory]): Category of the contact.<br> For more information,
                 see <a href='https://my.sevdesk.de/apiOverview/index.html#/doc-contacts#types'>here</a>.
        description (Union[Unset, str]): A description for the contact. Example: Rightful king of the seven kingdoms.
        academic_title (Union[Unset, str]): A academic title for the contact.
            Not to be used for organizations.
        gender (Union[Unset, str]): Gender of the contact.<br>
            Not to be used for organizations.
        sev_client (Union[Unset, ContactResponseModelSevClient]): Client to which contact belongs. Will be filled
            automatically
        name2 (Union[Unset, str]): Second name of the contact.<br>
            Not to be used for organizations. Example: Targaryen.
        birthday (Union[Unset, datetime.date]): Birthday of the contact.<br>
            Not to be used for organizations.
        vat_number (Union[Unset, str]): Vat number of the contact.
        bank_account (Union[Unset, str]): Bank account number (IBAN) of the contact.
        bank_number (Union[Unset, str]): Bank number of the bank used by the contact.
        default_cashback_time (Union[Unset, str]): Absolute time in days which the contact has to pay his invoices and
            subsequently get a cashback. Example: string.
        default_cashback_percent (Union[Unset, str]): Percentage of the invoice sum the contact gets back if he payed
            invoices in time. Example: string.
        default_time_to_pay (Union[Unset, str]): The payment goal in days which is set for every invoice of the contact.
            Example: string.
        tax_number (Union[Unset, str]): The tax number of the contact.
        tax_office (Union[Unset, str]): The tax office of the contact (only for greek customers). Example: string.
        exempt_vat (Union[Unset, str]): Defines if the contact is freed from paying vat. Example: false.
        tax_type (Union[Unset, ContactResponseModelTaxType]): Defines which tax regulation the contact is using.
        tax_set (Union[Unset, ContactResponseModelTaxSet]): Tax set which is used in every invoice of the contact.
        default_discount_amount (Union[Unset, str]): The default discount the contact gets for every invoice.<br>
            Depending on defaultDiscountPercentage attribute, in percent or absolute value. Example: string.
        default_discount_percentage (Union[Unset, str]): Defines if the discount is a percentage (true) or an absolute
            value (false). Example: false.
        buyer_reference (Union[Unset, str]): Buyer reference of the contact. Example: string.
        government_agency (Union[Unset, str]): Defines whether the contact is a government agency (true) or not (false).
            Example: false.
        additional_information (Union[Unset, str]): Additional information stored for the contact. Example: string.
    """

    id: Union[Unset, str] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    customer_number: Union[Unset, str] = UNSET
    parent: Union[Unset, "ContactResponseModelParent"] = UNSET
    surename: Union[Unset, str] = UNSET
    familyname: Union[Unset, str] = UNSET
    titel: Union[Unset, str] = UNSET
    category: Union[Unset, "ContactResponseModelCategory"] = UNSET
    description: Union[Unset, str] = UNSET
    academic_title: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    sev_client: Union[Unset, "ContactResponseModelSevClient"] = UNSET
    name2: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    vat_number: Union[Unset, str] = UNSET
    bank_account: Union[Unset, str] = UNSET
    bank_number: Union[Unset, str] = UNSET
    default_cashback_time: Union[Unset, str] = UNSET
    default_cashback_percent: Union[Unset, str] = UNSET
    default_time_to_pay: Union[Unset, str] = UNSET
    tax_number: Union[Unset, str] = UNSET
    tax_office: Union[Unset, str] = UNSET
    exempt_vat: Union[Unset, str] = UNSET
    tax_type: Union[Unset, ContactResponseModelTaxType] = UNSET
    tax_set: Union[Unset, "ContactResponseModelTaxSet"] = UNSET
    default_discount_amount: Union[Unset, str] = UNSET
    default_discount_percentage: Union[Unset, str] = UNSET
    buyer_reference: Union[Unset, str] = UNSET
    government_agency: Union[Unset, str] = UNSET
    additional_information: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        name = self.name
        status = self.status
        customer_number = self.customer_number
        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        surename = self.surename
        familyname = self.familyname
        titel = self.titel
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        description = self.description
        academic_title = self.academic_title
        gender = self.gender
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        name2 = self.name2
        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        vat_number = self.vat_number
        bank_account = self.bank_account
        bank_number = self.bank_number
        default_cashback_time = self.default_cashback_time
        default_cashback_percent = self.default_cashback_percent
        default_time_to_pay = self.default_time_to_pay
        tax_number = self.tax_number
        tax_office = self.tax_office
        exempt_vat = self.exempt_vat
        tax_type: Union[Unset, str] = UNSET
        if not isinstance(self.tax_type, Unset):
            tax_type = self.tax_type.value

        tax_set: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_set, Unset):
            tax_set = self.tax_set.to_dict()

        default_discount_amount = self.default_discount_amount
        default_discount_percentage = self.default_discount_percentage
        buyer_reference = self.buyer_reference
        government_agency = self.government_agency
        additional_information = self.additional_information

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if status is not UNSET:
            field_dict["status"] = status
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
        if category is not UNSET:
            field_dict["category"] = category
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
        if buyer_reference is not UNSET:
            field_dict["buyerReference"] = buyer_reference
        if government_agency is not UNSET:
            field_dict["governmentAgency"] = government_agency
        if additional_information is not UNSET:
            field_dict["additionalInformation"] = additional_information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_response_model_category import (
            ContactResponseModelCategory,
        )
        from ..models.contact_response_model_parent import ContactResponseModelParent
        from ..models.contact_response_model_sev_client import (
            ContactResponseModelSevClient,
        )
        from ..models.contact_response_model_tax_set import ContactResponseModelTaxSet

        d = src_dict.copy()
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

        status = d.pop("status", UNSET)

        customer_number = d.pop("customerNumber", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, ContactResponseModelParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ContactResponseModelParent.from_dict(_parent)

        surename = d.pop("surename", UNSET)

        familyname = d.pop("familyname", UNSET)

        titel = d.pop("titel", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, ContactResponseModelCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ContactResponseModelCategory.from_dict(_category)

        description = d.pop("description", UNSET)

        academic_title = d.pop("academicTitle", UNSET)

        gender = d.pop("gender", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, ContactResponseModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = ContactResponseModelSevClient.from_dict(_sev_client)

        name2 = d.pop("name2", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.date]
        if isinstance(_birthday, Unset):
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
        tax_type: Union[Unset, ContactResponseModelTaxType]
        if isinstance(_tax_type, Unset):
            tax_type = UNSET
        else:
            tax_type = ContactResponseModelTaxType(_tax_type)

        _tax_set = d.pop("taxSet", UNSET)
        tax_set: Union[Unset, ContactResponseModelTaxSet]
        if isinstance(_tax_set, Unset):
            tax_set = UNSET
        else:
            tax_set = ContactResponseModelTaxSet.from_dict(_tax_set)

        default_discount_amount = d.pop("defaultDiscountAmount", UNSET)

        default_discount_percentage = d.pop("defaultDiscountPercentage", UNSET)

        buyer_reference = d.pop("buyerReference", UNSET)

        government_agency = d.pop("governmentAgency", UNSET)

        additional_information = d.pop("additionalInformation", UNSET)

        contact_response_model = cls(
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            name=name,
            status=status,
            customer_number=customer_number,
            parent=parent,
            surename=surename,
            familyname=familyname,
            titel=titel,
            category=category,
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
            buyer_reference=buyer_reference,
            government_agency=government_agency,
            additional_information=additional_information,
        )

        contact_response_model.additional_properties = d
        return contact_response_model

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
