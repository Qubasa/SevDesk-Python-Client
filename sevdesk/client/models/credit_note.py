import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.credit_note_accounting_type import CreditNoteAccountingType
from ..models.credit_note_booking_category import CreditNoteBookingCategory
from ..models.credit_note_credit_note_type import CreditNoteCreditNoteType
from ..models.credit_note_ref_src_invoice import CreditNoteRefSrcInvoice
from ..models.document_model_address_contact_ref import DocumentModelAddressContactRef
from ..models.document_model_address_country import DocumentModelAddressCountry
from ..models.document_model_contact import DocumentModelContact
from ..models.document_model_contact_person import DocumentModelContactPerson
from ..models.document_model_cost_centre import DocumentModelCostCentre
from ..models.document_model_create_user import DocumentModelCreateUser
from ..models.document_model_datev_connect_online import DocumentModelDatevConnectOnline
from ..models.document_model_entry_type import DocumentModelEntryType
from ..models.document_model_origin import DocumentModelOrigin
from ..models.document_model_payment_method import DocumentModelPaymentMethod
from ..models.document_model_send_type import DocumentModelSendType
from ..models.document_model_sev_client import DocumentModelSevClient
from ..models.document_model_status import DocumentModelStatus
from ..models.document_model_tax_set import DocumentModelTaxSet
from ..models.document_model_tax_type import DocumentModelTaxType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditNote")


@attr.s(auto_attribs=True)
class CreditNote:
    """
    Attributes:
        contact (DocumentModelContact): The contact used in the document
        discount (int): If you want to give a discount, define the percentage here. Otherwise provide zero as value
        delivery_date (datetime.datetime): Timestamp. This can also be a date range if you also use the attribute
            deliveryDateUntil Example: 01.01.20.
        status (DocumentModelStatus): Please have a look in docs to see what the different status codes mean Example:
            100.
        small_settlement (bool): Defines if the client uses the small settlement scheme. If yes, the document must not
            contain any vat
        contact_person (DocumentModelContactPerson): The user who acts as a contact person for the document
        tax_rate (float): Is overwritten by document position tax rates Example: 19.
        tax_text (str): A common tax text would be 'Umsatzsteuer 19%' Example: Umsatzsteuer 19%.
        tax_type (DocumentModelTaxType): Tax type of the document. There are four tax types: 1. default - Umsatzsteuer
            ausweisen, 2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union), 3. noteu -
            Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz), 4. custom - Using custom tax set.
            Tax rates are heavily connected to the tax type used. Default: DocumentModelTaxType.DEFAULT.
        currency (str): Currency used in the document. Needs to be currency code according to ISO-4217 Default: 'EUR'.
        booking_category (CreditNoteBookingCategory): The credit note booking category
        credit_note_date (datetime.datetime): Needs to be provided as timestamp or dd.mm.yyyy Example: 01.01.20.
        credit_note_type (CreditNoteCreditNoteType):  Default: CreditNoteCreditNoteType.CN.
        id (Union[Unset, None, int]): The document id
        create (Union[Unset, datetime.datetime]): Date of document creation
        update (Union[Unset, datetime.datetime]): Date of last document update
        sev_client (Union[Unset, DocumentModelSevClient]): Client to which document belongs. Will be filled
            automatically
        header (Union[Unset, None, str]): Normally consist of prefix plus the document number
        head_text (Union[Unset, None, str]): Certain html tags can be used here to format your text
        foot_text (Union[Unset, None, str]): Certain html tags can be used here to format your text
        time_to_pay (Union[Unset, None, int]): The time the customer has to pay the document in days
        discount_time (Union[Unset, None, int]): If a value other than zero is used for the discount attribute, you need
            to specify the amount of days for which the discount is granted.
        address_name (Union[Unset, None, str]): Can be omitted as complete address is defined in address attribute
        address_street (Union[Unset, None, str]): Can be omitted as complete address is defined in address attribute
        address_zip (Union[Unset, None, str]): Can be omitted as complete address is defined in address attribute
        address_city (Union[Unset, None, str]): Can be omitted as complete address is defined in address attribute
        address_country (Union[Unset, DocumentModelAddressCountry]):
        pay_date (Union[Unset, None, datetime.datetime]): Needs to be timestamp or dd.mm.yyyy
        create_user (Union[Unset, DocumentModelCreateUser]): Will be filled automatically by our system and can't be
            changed
        dunning_level (Union[Unset, None, int]): Defines how many reminders have already been sent for the document.
            Starts with 1 (Payment reminder) and should be incremented by one every time another reminder is sent.
        address_parent_name (Union[Unset, None, str]): Address parent name.
        address_contact_ref (Union[Unset, None, DocumentModelAddressContactRef]): Address contact reference.
        payment_method (Union[Unset, DocumentModelPaymentMethod]): Payment method used for the document
        cost_centre (Union[Unset, DocumentModelCostCentre]): Cost centre for the document
        send_date (Union[Unset, None, datetime.datetime]): The date the document was sent to the customer
        origin (Union[Unset, None, DocumentModelOrigin]): Origin of the document. Could f.e. be an order
        reminder_total (Union[Unset, None, float]): Total reminder amount
        reminder_debit (Union[Unset, None, float]): Debit of the reminder
        reminder_deadline (Union[Unset, None, int]): Deadline of the reminder as timestamp
        reminder_charge (Union[Unset, None, float]): The additional reminder charge
        address_parent_name_2 (Union[Unset, None, str]): Deprecated attribute
        address_name_2 (Union[Unset, None, str]): Second name of the recipient
        tax_set (Union[Unset, None, DocumentModelTaxSet]): Tax set of the document. Needs to be added if you chose the
            tax type custom
        address_gender (Union[Unset, None, str]): Gender of the recipient
        account_end_date (Union[Unset, None, int]): Deprecated attribute.
        address (Union[Unset, None, str]): Complete address of the recipient including name, street, city, zip and
            country. Line breaks can be used and will be displayed on the document pdf.
        sum_net (Union[Unset, float]): Net sum of the document
        sum_tax (Union[Unset, float]): Tax sum of the document
        sum_gross (Union[Unset, float]): Gross sum of the document
        sum_discounts (Union[Unset, float]): Sum of all discounts in the document
        sum_net_foreign_currency (Union[Unset, float]): Net sum of the document in the foreign currency
        sum_tax_foreign_currency (Union[Unset, float]): Tax sum of the document in the foreign currency
        sum_gross_foreign_currency (Union[Unset, float]): Gross sum of the document in the foreign currency
        sum_discounts_foreign_currency (Union[Unset, float]): Discounts sum of the document in the foreign currency
        sum_net_accounting (Union[Unset, float]): Net accounting sum of the document. Is usually the same as sumNet
        sum_tax_accounting (Union[Unset, float]): Tax accounting sum of the document. Is usually the same as sumTax
        sum_gross_accounting (Union[Unset, float]): Gross accounting sum of the document. Is usually the same as
            sumGross
        paid_amount (Union[Unset, None, float]): Amount which has already been paid for this document by the customer
        entry_type (Union[Unset, None, DocumentModelEntryType]): Deprecated attribute.
        customer_internal_note (Union[Unset, None, str]): Internal note of the customer. Contains data entered into
            field 'Referenz/Bestellnummer'
        show_net (Union[Unset, bool]): If true, the net amount of each position will be shown on the document. Otherwise
            gross amount Default: True.
        enshrined (Union[Unset, None, datetime.datetime]): Defines if and when document was enshrined. Enshrined
            documents can not be manipulated.
        send_type (Union[Unset, None, DocumentModelSendType]): Type which was used to send the document.
        delivery_date_until (Union[Unset, None, int]): If the delivery date should be a time range, another timestamp
            can be provided in this attribute to define a range from timestamp used in deliveryDate attribute to the
            timestamp used here.
        datev_connect_online (Union[Unset, None, DocumentModelDatevConnectOnline]): Internal attribute
        send_payment_received_notification_date (Union[Unset, None, int]): Internal attribute
        ref_src_invoice (Union[Unset, None, CreditNoteRefSrcInvoice]): The invoice from which the underachievement
            originates - for booking category UNDERACHIEVEMENT
        accounting_type (Union[Unset, None, CreditNoteAccountingType]): The account on which this credit note should be
            booked - for booking category ACCOUNTING_TYPE
        object_name (Union[Unset, str]): The document object name Default: 'CreditNote'.
        credit_note_number (Union[Unset, None, str]): The credit note number Example: GU-1000.
        tax_number (Union[Unset, None, str]): The TAX number of receiving customer
        vat_number (Union[Unset, None, str]): The VAT number of receiving customer
    """

    contact: DocumentModelContact
    delivery_date: datetime.datetime
    status: DocumentModelStatus
    small_settlement: bool
    contact_person: DocumentModelContactPerson
    tax_rate: float
    tax_text: str
    booking_category: CreditNoteBookingCategory
    credit_note_date: datetime.datetime
    discount: int = 0
    tax_type: DocumentModelTaxType = DocumentModelTaxType.DEFAULT
    currency: str = "EUR"
    credit_note_type: CreditNoteCreditNoteType = CreditNoteCreditNoteType.CN
    id: Union[Unset, None, int] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    sev_client: Union[Unset, DocumentModelSevClient] = UNSET
    header: Union[Unset, None, str] = UNSET
    head_text: Union[Unset, None, str] = UNSET
    foot_text: Union[Unset, None, str] = UNSET
    time_to_pay: Union[Unset, None, int] = UNSET
    discount_time: Union[Unset, None, int] = UNSET
    address_name: Union[Unset, None, str] = UNSET
    address_street: Union[Unset, None, str] = UNSET
    address_zip: Union[Unset, None, str] = UNSET
    address_city: Union[Unset, None, str] = UNSET
    address_country: Union[Unset, DocumentModelAddressCountry] = UNSET
    pay_date: Union[Unset, None, datetime.datetime] = UNSET
    create_user: Union[Unset, DocumentModelCreateUser] = UNSET
    dunning_level: Union[Unset, None, int] = UNSET
    address_parent_name: Union[Unset, None, str] = UNSET
    address_contact_ref: Union[Unset, None, DocumentModelAddressContactRef] = UNSET
    payment_method: Union[Unset, DocumentModelPaymentMethod] = UNSET
    cost_centre: Union[Unset, DocumentModelCostCentre] = UNSET
    send_date: Union[Unset, None, datetime.datetime] = UNSET
    origin: Union[Unset, None, DocumentModelOrigin] = UNSET
    reminder_total: Union[Unset, None, float] = UNSET
    reminder_debit: Union[Unset, None, float] = UNSET
    reminder_deadline: Union[Unset, None, int] = UNSET
    reminder_charge: Union[Unset, None, float] = UNSET
    address_parent_name_2: Union[Unset, None, str] = UNSET
    address_name_2: Union[Unset, None, str] = UNSET
    tax_set: Union[Unset, None, DocumentModelTaxSet] = UNSET
    address_gender: Union[Unset, None, str] = UNSET
    account_end_date: Union[Unset, None, int] = UNSET
    address: Union[Unset, None, str] = UNSET
    sum_net: Union[Unset, float] = UNSET
    sum_tax: Union[Unset, float] = UNSET
    sum_gross: Union[Unset, float] = UNSET
    sum_discounts: Union[Unset, float] = UNSET
    sum_net_foreign_currency: Union[Unset, float] = UNSET
    sum_tax_foreign_currency: Union[Unset, float] = UNSET
    sum_gross_foreign_currency: Union[Unset, float] = UNSET
    sum_discounts_foreign_currency: Union[Unset, float] = UNSET
    sum_net_accounting: Union[Unset, float] = UNSET
    sum_tax_accounting: Union[Unset, float] = UNSET
    sum_gross_accounting: Union[Unset, float] = UNSET
    paid_amount: Union[Unset, None, float] = UNSET
    entry_type: Union[Unset, None, DocumentModelEntryType] = UNSET
    customer_internal_note: Union[Unset, None, str] = UNSET
    show_net: Union[Unset, bool] = True
    enshrined: Union[Unset, None, datetime.datetime] = UNSET
    send_type: Union[Unset, None, DocumentModelSendType] = UNSET
    delivery_date_until: Union[Unset, None, int] = UNSET
    datev_connect_online: Union[Unset, None, DocumentModelDatevConnectOnline] = UNSET
    send_payment_received_notification_date: Union[Unset, None, int] = UNSET
    ref_src_invoice: Union[Unset, None, CreditNoteRefSrcInvoice] = UNSET
    accounting_type: Union[Unset, None, CreditNoteAccountingType] = UNSET
    object_name: Union[Unset, str] = "CreditNote"
    credit_note_number: Union[Unset, None, str] = UNSET
    tax_number: Union[Unset, None, str] = UNSET
    vat_number: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact.to_dict()

        discount = self.discount
        delivery_date = self.delivery_date.isoformat()

        status = self.status.value

        small_settlement = self.small_settlement
        contact_person = self.contact_person.to_dict()

        tax_rate = self.tax_rate
        tax_text = self.tax_text
        tax_type = self.tax_type.value

        currency = self.currency
        booking_category = self.booking_category.value

        credit_note_date = self.credit_note_date.isoformat()

        credit_note_type = self.credit_note_type.value

        id = self.id
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        header = self.header
        head_text = self.head_text
        foot_text = self.foot_text
        time_to_pay = self.time_to_pay
        discount_time = self.discount_time
        address_name = self.address_name
        address_street = self.address_street
        address_zip = self.address_zip
        address_city = self.address_city
        address_country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_country, Unset):
            address_country = self.address_country.to_dict()

        pay_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.pay_date, Unset):
            pay_date = self.pay_date.isoformat() if self.pay_date else None

        create_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_user, Unset):
            create_user = self.create_user.to_dict()

        dunning_level = self.dunning_level
        address_parent_name = self.address_parent_name
        address_contact_ref: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.address_contact_ref, Unset):
            address_contact_ref = (
                self.address_contact_ref.to_dict() if self.address_contact_ref else None
            )

        payment_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.to_dict()

        cost_centre: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_centre, Unset):
            cost_centre = self.cost_centre.to_dict()

        send_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.send_date, Unset):
            send_date = self.send_date.isoformat() if self.send_date else None

        origin: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict() if self.origin else None

        reminder_total = self.reminder_total
        reminder_debit = self.reminder_debit
        reminder_deadline = self.reminder_deadline
        reminder_charge = self.reminder_charge
        address_parent_name_2 = self.address_parent_name_2
        address_name_2 = self.address_name_2
        tax_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_set, Unset):
            tax_set = self.tax_set.to_dict() if self.tax_set else None

        address_gender = self.address_gender
        account_end_date = self.account_end_date
        address = self.address
        sum_net = self.sum_net
        sum_tax = self.sum_tax
        sum_gross = self.sum_gross
        sum_discounts = self.sum_discounts
        sum_net_foreign_currency = self.sum_net_foreign_currency
        sum_tax_foreign_currency = self.sum_tax_foreign_currency
        sum_gross_foreign_currency = self.sum_gross_foreign_currency
        sum_discounts_foreign_currency = self.sum_discounts_foreign_currency
        sum_net_accounting = self.sum_net_accounting
        sum_tax_accounting = self.sum_tax_accounting
        sum_gross_accounting = self.sum_gross_accounting
        paid_amount = self.paid_amount
        entry_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.entry_type, Unset):
            entry_type = self.entry_type.to_dict() if self.entry_type else None

        customer_internal_note = self.customer_internal_note
        show_net = self.show_net
        enshrined: Union[Unset, None, str] = UNSET
        if not isinstance(self.enshrined, Unset):
            enshrined = self.enshrined.isoformat() if self.enshrined else None

        send_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.send_type, Unset):
            send_type = self.send_type.value if self.send_type else None

        delivery_date_until = self.delivery_date_until
        datev_connect_online: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.datev_connect_online, Unset):
            datev_connect_online = (
                self.datev_connect_online.to_dict()
                if self.datev_connect_online
                else None
            )

        send_payment_received_notification_date = (
            self.send_payment_received_notification_date
        )
        ref_src_invoice: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.ref_src_invoice, Unset):
            ref_src_invoice = (
                self.ref_src_invoice.to_dict() if self.ref_src_invoice else None
            )

        accounting_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.accounting_type, Unset):
            accounting_type = (
                self.accounting_type.to_dict() if self.accounting_type else None
            )

        object_name = self.object_name
        credit_note_number = self.credit_note_number
        tax_number = self.tax_number
        vat_number = self.vat_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "discount": discount,
                "deliveryDate": delivery_date,
                "status": status,
                "smallSettlement": small_settlement,
                "contactPerson": contact_person,
                "taxRate": tax_rate,
                "taxText": tax_text,
                "taxType": tax_type,
                "currency": currency,
                "bookingCategory": booking_category,
                "creditNoteDate": credit_note_date,
                "creditNoteType": credit_note_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if header is not UNSET:
            field_dict["header"] = header
        if head_text is not UNSET:
            field_dict["headText"] = head_text
        if foot_text is not UNSET:
            field_dict["footText"] = foot_text
        if time_to_pay is not UNSET:
            field_dict["timeToPay"] = time_to_pay
        if discount_time is not UNSET:
            field_dict["discountTime"] = discount_time
        if address_name is not UNSET:
            field_dict["addressName"] = address_name
        if address_street is not UNSET:
            field_dict["addressStreet"] = address_street
        if address_zip is not UNSET:
            field_dict["addressZip"] = address_zip
        if address_city is not UNSET:
            field_dict["addressCity"] = address_city
        if address_country is not UNSET:
            field_dict["addressCountry"] = address_country
        if pay_date is not UNSET:
            field_dict["payDate"] = pay_date
        if create_user is not UNSET:
            field_dict["createUser"] = create_user
        if dunning_level is not UNSET:
            field_dict["dunningLevel"] = dunning_level
        if address_parent_name is not UNSET:
            field_dict["addressParentName"] = address_parent_name
        if address_contact_ref is not UNSET:
            field_dict["addressContactRef"] = address_contact_ref
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if cost_centre is not UNSET:
            field_dict["costCentre"] = cost_centre
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date
        if origin is not UNSET:
            field_dict["origin"] = origin
        if reminder_total is not UNSET:
            field_dict["reminderTotal"] = reminder_total
        if reminder_debit is not UNSET:
            field_dict["reminderDebit"] = reminder_debit
        if reminder_deadline is not UNSET:
            field_dict["reminderDeadline"] = reminder_deadline
        if reminder_charge is not UNSET:
            field_dict["reminderCharge"] = reminder_charge
        if address_parent_name_2 is not UNSET:
            field_dict["addressParentName2"] = address_parent_name_2
        if address_name_2 is not UNSET:
            field_dict["addressName2"] = address_name_2
        if tax_set is not UNSET:
            field_dict["taxSet"] = tax_set
        if address_gender is not UNSET:
            field_dict["addressGender"] = address_gender
        if account_end_date is not UNSET:
            field_dict["accountEndDate"] = account_end_date
        if address is not UNSET:
            field_dict["address"] = address
        if sum_net is not UNSET:
            field_dict["sumNet"] = sum_net
        if sum_tax is not UNSET:
            field_dict["sumTax"] = sum_tax
        if sum_gross is not UNSET:
            field_dict["sumGross"] = sum_gross
        if sum_discounts is not UNSET:
            field_dict["sumDiscounts"] = sum_discounts
        if sum_net_foreign_currency is not UNSET:
            field_dict["sumNetForeignCurrency"] = sum_net_foreign_currency
        if sum_tax_foreign_currency is not UNSET:
            field_dict["sumTaxForeignCurrency"] = sum_tax_foreign_currency
        if sum_gross_foreign_currency is not UNSET:
            field_dict["sumGrossForeignCurrency"] = sum_gross_foreign_currency
        if sum_discounts_foreign_currency is not UNSET:
            field_dict["sumDiscountsForeignCurrency"] = sum_discounts_foreign_currency
        if sum_net_accounting is not UNSET:
            field_dict["sumNetAccounting"] = sum_net_accounting
        if sum_tax_accounting is not UNSET:
            field_dict["sumTaxAccounting"] = sum_tax_accounting
        if sum_gross_accounting is not UNSET:
            field_dict["sumGrossAccounting"] = sum_gross_accounting
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if customer_internal_note is not UNSET:
            field_dict["customerInternalNote"] = customer_internal_note
        if show_net is not UNSET:
            field_dict["showNet"] = show_net
        if enshrined is not UNSET:
            field_dict["enshrined"] = enshrined
        if send_type is not UNSET:
            field_dict["sendType"] = send_type
        if delivery_date_until is not UNSET:
            field_dict["deliveryDateUntil"] = delivery_date_until
        if datev_connect_online is not UNSET:
            field_dict["datevConnectOnline"] = datev_connect_online
        if send_payment_received_notification_date is not UNSET:
            field_dict[
                "sendPaymentReceivedNotificationDate"
            ] = send_payment_received_notification_date
        if ref_src_invoice is not UNSET:
            field_dict["refSrcInvoice"] = ref_src_invoice
        if accounting_type is not UNSET:
            field_dict["accountingType"] = accounting_type
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if credit_note_number is not UNSET:
            field_dict["creditNoteNumber"] = credit_note_number
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact = DocumentModelContact.from_dict(d.pop("contact"))

        discount = d.pop("discount")

        delivery_date = isoparse(d.pop("deliveryDate"))

        status = DocumentModelStatus(d.pop("status"))

        small_settlement = d.pop("smallSettlement")

        contact_person = DocumentModelContactPerson.from_dict(d.pop("contactPerson"))

        tax_rate = d.pop("taxRate")

        tax_text = d.pop("taxText")

        tax_type = DocumentModelTaxType(d.pop("taxType"))

        currency = d.pop("currency")

        booking_category = CreditNoteBookingCategory(d.pop("bookingCategory"))

        credit_note_date = isoparse(d.pop("creditNoteDate"))

        credit_note_type = CreditNoteCreditNoteType(d.pop("creditNoteType"))

        id = d.pop("id", UNSET)

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

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, DocumentModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = DocumentModelSevClient.from_dict(_sev_client)

        header = d.pop("header", UNSET)

        head_text = d.pop("headText", UNSET)

        foot_text = d.pop("footText", UNSET)

        time_to_pay = d.pop("timeToPay", UNSET)

        discount_time = d.pop("discountTime", UNSET)

        address_name = d.pop("addressName", UNSET)

        address_street = d.pop("addressStreet", UNSET)

        address_zip = d.pop("addressZip", UNSET)

        address_city = d.pop("addressCity", UNSET)

        _address_country = d.pop("addressCountry", UNSET)
        address_country: Union[Unset, DocumentModelAddressCountry]
        if isinstance(_address_country, Unset):
            address_country = UNSET
        else:
            address_country = DocumentModelAddressCountry.from_dict(_address_country)

        _pay_date = d.pop("payDate", UNSET)
        pay_date: Union[Unset, None, datetime.datetime]
        if _pay_date is None:
            pay_date = None
        elif isinstance(_pay_date, Unset):
            pay_date = UNSET
        else:
            pay_date = isoparse(_pay_date)

        _create_user = d.pop("createUser", UNSET)
        create_user: Union[Unset, DocumentModelCreateUser]
        if isinstance(_create_user, Unset):
            create_user = UNSET
        else:
            create_user = DocumentModelCreateUser.from_dict(_create_user)

        dunning_level = d.pop("dunningLevel", UNSET)

        address_parent_name = d.pop("addressParentName", UNSET)

        _address_contact_ref = d.pop("addressContactRef", UNSET)
        address_contact_ref: Union[Unset, None, DocumentModelAddressContactRef]
        if _address_contact_ref is None:
            address_contact_ref = None
        elif isinstance(_address_contact_ref, Unset):
            address_contact_ref = UNSET
        else:
            address_contact_ref = DocumentModelAddressContactRef.from_dict(
                _address_contact_ref
            )

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, DocumentModelPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = DocumentModelPaymentMethod.from_dict(_payment_method)

        _cost_centre = d.pop("costCentre", UNSET)
        cost_centre: Union[Unset, DocumentModelCostCentre]
        if isinstance(_cost_centre, Unset):
            cost_centre = UNSET
        else:
            cost_centre = DocumentModelCostCentre.from_dict(_cost_centre)

        _send_date = d.pop("sendDate", UNSET)
        send_date: Union[Unset, None, datetime.datetime]
        if _send_date is None:
            send_date = None
        elif isinstance(_send_date, Unset):
            send_date = UNSET
        else:
            send_date = isoparse(_send_date)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, None, DocumentModelOrigin]
        if _origin is None:
            origin = None
        elif isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = DocumentModelOrigin.from_dict(_origin)

        reminder_total = d.pop("reminderTotal", UNSET)

        reminder_debit = d.pop("reminderDebit", UNSET)

        reminder_deadline = d.pop("reminderDeadline", UNSET)

        reminder_charge = d.pop("reminderCharge", UNSET)

        address_parent_name_2 = d.pop("addressParentName2", UNSET)

        address_name_2 = d.pop("addressName2", UNSET)

        _tax_set = d.pop("taxSet", UNSET)
        tax_set: Union[Unset, None, DocumentModelTaxSet]
        if _tax_set is None:
            tax_set = None
        elif isinstance(_tax_set, Unset):
            tax_set = UNSET
        else:
            tax_set = DocumentModelTaxSet.from_dict(_tax_set)

        address_gender = d.pop("addressGender", UNSET)

        account_end_date = d.pop("accountEndDate", UNSET)

        address = d.pop("address", UNSET)

        sum_net = d.pop("sumNet", UNSET)

        sum_tax = d.pop("sumTax", UNSET)

        sum_gross = d.pop("sumGross", UNSET)

        sum_discounts = d.pop("sumDiscounts", UNSET)

        sum_net_foreign_currency = d.pop("sumNetForeignCurrency", UNSET)

        sum_tax_foreign_currency = d.pop("sumTaxForeignCurrency", UNSET)

        sum_gross_foreign_currency = d.pop("sumGrossForeignCurrency", UNSET)

        sum_discounts_foreign_currency = d.pop("sumDiscountsForeignCurrency", UNSET)

        sum_net_accounting = d.pop("sumNetAccounting", UNSET)

        sum_tax_accounting = d.pop("sumTaxAccounting", UNSET)

        sum_gross_accounting = d.pop("sumGrossAccounting", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        _entry_type = d.pop("entryType", UNSET)
        entry_type: Union[Unset, None, DocumentModelEntryType]
        if _entry_type is None:
            entry_type = None
        elif isinstance(_entry_type, Unset):
            entry_type = UNSET
        else:
            entry_type = DocumentModelEntryType.from_dict(_entry_type)

        customer_internal_note = d.pop("customerInternalNote", UNSET)

        show_net = d.pop("showNet", UNSET)

        _enshrined = d.pop("enshrined", UNSET)
        enshrined: Union[Unset, None, datetime.datetime]
        if _enshrined is None:
            enshrined = None
        elif isinstance(_enshrined, Unset):
            enshrined = UNSET
        else:
            enshrined = isoparse(_enshrined)

        _send_type = d.pop("sendType", UNSET)
        send_type: Union[Unset, None, DocumentModelSendType]
        if _send_type is None:
            send_type = None
        elif isinstance(_send_type, Unset):
            send_type = UNSET
        else:
            send_type = DocumentModelSendType(_send_type)

        delivery_date_until = d.pop("deliveryDateUntil", UNSET)

        _datev_connect_online = d.pop("datevConnectOnline", UNSET)
        datev_connect_online: Union[Unset, None, DocumentModelDatevConnectOnline]
        if _datev_connect_online is None:
            datev_connect_online = None
        elif isinstance(_datev_connect_online, Unset):
            datev_connect_online = UNSET
        else:
            datev_connect_online = DocumentModelDatevConnectOnline.from_dict(
                _datev_connect_online
            )

        send_payment_received_notification_date = d.pop(
            "sendPaymentReceivedNotificationDate", UNSET
        )

        _ref_src_invoice = d.pop("refSrcInvoice", UNSET)
        ref_src_invoice: Union[Unset, None, CreditNoteRefSrcInvoice]
        if _ref_src_invoice is None:
            ref_src_invoice = None
        elif isinstance(_ref_src_invoice, Unset):
            ref_src_invoice = UNSET
        else:
            ref_src_invoice = CreditNoteRefSrcInvoice.from_dict(_ref_src_invoice)

        _accounting_type = d.pop("accountingType", UNSET)
        accounting_type: Union[Unset, None, CreditNoteAccountingType]
        if _accounting_type is None:
            accounting_type = None
        elif isinstance(_accounting_type, Unset):
            accounting_type = UNSET
        else:
            accounting_type = CreditNoteAccountingType.from_dict(_accounting_type)

        object_name = d.pop("objectName", UNSET)

        credit_note_number = d.pop("creditNoteNumber", UNSET)

        tax_number = d.pop("taxNumber", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        credit_note = cls(
            contact=contact,
            discount=discount,
            delivery_date=delivery_date,
            status=status,
            small_settlement=small_settlement,
            contact_person=contact_person,
            tax_rate=tax_rate,
            tax_text=tax_text,
            tax_type=tax_type,
            currency=currency,
            booking_category=booking_category,
            credit_note_date=credit_note_date,
            credit_note_type=credit_note_type,
            id=id,
            create=create,
            update=update,
            sev_client=sev_client,
            header=header,
            head_text=head_text,
            foot_text=foot_text,
            time_to_pay=time_to_pay,
            discount_time=discount_time,
            address_name=address_name,
            address_street=address_street,
            address_zip=address_zip,
            address_city=address_city,
            address_country=address_country,
            pay_date=pay_date,
            create_user=create_user,
            dunning_level=dunning_level,
            address_parent_name=address_parent_name,
            address_contact_ref=address_contact_ref,
            payment_method=payment_method,
            cost_centre=cost_centre,
            send_date=send_date,
            origin=origin,
            reminder_total=reminder_total,
            reminder_debit=reminder_debit,
            reminder_deadline=reminder_deadline,
            reminder_charge=reminder_charge,
            address_parent_name_2=address_parent_name_2,
            address_name_2=address_name_2,
            tax_set=tax_set,
            address_gender=address_gender,
            account_end_date=account_end_date,
            address=address,
            sum_net=sum_net,
            sum_tax=sum_tax,
            sum_gross=sum_gross,
            sum_discounts=sum_discounts,
            sum_net_foreign_currency=sum_net_foreign_currency,
            sum_tax_foreign_currency=sum_tax_foreign_currency,
            sum_gross_foreign_currency=sum_gross_foreign_currency,
            sum_discounts_foreign_currency=sum_discounts_foreign_currency,
            sum_net_accounting=sum_net_accounting,
            sum_tax_accounting=sum_tax_accounting,
            sum_gross_accounting=sum_gross_accounting,
            paid_amount=paid_amount,
            entry_type=entry_type,
            customer_internal_note=customer_internal_note,
            show_net=show_net,
            enshrined=enshrined,
            send_type=send_type,
            delivery_date_until=delivery_date_until,
            datev_connect_online=datev_connect_online,
            send_payment_received_notification_date=send_payment_received_notification_date,
            ref_src_invoice=ref_src_invoice,
            accounting_type=accounting_type,
            object_name=object_name,
            credit_note_number=credit_note_number,
            tax_number=tax_number,
            vat_number=vat_number,
        )

        credit_note.additional_properties = d
        return credit_note

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
