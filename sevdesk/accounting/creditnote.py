from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Union

import attrs

from sevdesk.client.models.credit_note_position import CreditNotePosition

from .. import UNSET, Client, Unset
from ..client.api.credit_note import (
    create_credit_note_by_factory,
    credit_note_change_status,
    credit_note_get_pdf,
    delete_credit_note,
    get_credit_notes,
    get_next_credit_note_number,
)
from ..client.api.credit_note_discounts import get_credit_note_discounts_by_id
from ..client.api.credit_note_pos import get_credit_note_pos
from ..client.models import (
    CreateCreditNoteByFactoryJsonBody,
    CreateCreditNoteByFactoryResponse201,
    CreateCreditNoteByFactoryResponse201Objects,
    CreditNoteAccountingType,
    CreditNoteBookingCategory,
    CreditNoteChangeStatusJsonBody,
    CreditNoteChangeStatusJsonBodyValue,
    CreditNoteRefSrcInvoice,
    DocumentModelAddressCountry,
    DocumentModelContact,
    DocumentModelContactPerson,
    DocumentModelStatus,
    FactoryCreditNote,
    FactoryCreditNotePositionSave,
    FactoryDiscountSave,
)
from ..common import SevDesk, SevUser
from ..contact import Contact
from .category import AccountingType
from .discount import Discount
from .invoice import Invoice
from .lineitem import LineItem
from .pdf import Pdf

# TODO Create CreditNote corresponding to an invoice
# TODO Create a new CreditNote for accounting


class BookingCategory(str, Enum):
    PROVISION = "PROVISION"
    ROYALTY_ASSIGNED = "ROYALTY_ASSIGNED"
    ROYALTY_UNASSIGNED = "ROYALTY_UNASSIGNED"
    UNDERACHIEVEMENT = "UNDERACHIEVEMENT"
    ACCOUNTING_TYPE = "ACCOUNTING_TYPE"

    def _get_api_model(self, client: Client) -> CreditNoteBookingCategory:
        return CreditNoteBookingCategory(self.value)


class CreditNoteStatus(Enum):
    DRAFT = DocumentModelStatus.VALUE_1
    OPEN = DocumentModelStatus.VALUE_2
    PAYED = DocumentModelStatus.VALUE_3

    def _get_api_model(self, client: Client) -> DocumentModelStatus:
        return self.value


@attrs.define()
class CreditNote:
    """
    A simplified helper to create credit notes in SevDesk.
    The class is optimised for Shopify, but covers the most common use-cases.
    """

    booking_category: BookingCategory = attrs.field(on_setattr=attrs.setters.frozen)
    "The credit note booking category"
    customer: Contact = attrs.field(on_setattr=attrs.setters.frozen)
    "The customer the credit note belongs to. After the credit note is created, make sure to not change the customer anymore."
    header: str
    "The credit note header, e.g. 'Gutschrift zu Auftrag #1000'"
    reference: Union[Unset, str] = attrs.field(on_setattr=attrs.setters.frozen)
    "The reference allows the API to filter for a specific credit-note."
    "A Shopify Client could use the reference to store the Shopify API ID"
    status: CreditNoteStatus = CreditNoteStatus.DRAFT
    "Credit-Note-Status"
    items: Union[Unset, List[LineItem]] = UNSET
    "Credit-Note-Items"
    id: Union[Unset, str] = UNSET
    "Internal parameter of the credit note ID. Will be set when creted."
    credit_note_date: Union[Unset, datetime] = UNSET
    "Credit Note timestamp. If not set, datetime.now() will be called on initialisation of the credit note object."
    delivery_date: Union[Unset, datetime] = UNSET
    "Delivery timestamp. If not set, credit_note_date will be used as delivery_date."
    small_settlement: bool = False
    "Defines if the client uses the small settlement scheme. If yes, the credit note must not contain any vat."
    # TODO Make this an environment-variable parameter
    tax_rate: float = 20.0
    "Default tax-rate, overwritten by the line item."
    # TODO Make an environment-variable parameter
    tax_text: Union[Unset, str] = UNSET
    "Default tax-text, will be automatically set to Mehrwertssteuer {tax_rate}%"
    contact_person: Union[Unset, SevUser] = UNSET
    "The contact person. If not given, the SevUser corresponding to the API-Token will be used"
    credit_note_number: Union[Unset, str] = UNSET
    "The credit note number. If not set, the next number will be queried from SevDesk on calling the create function."
    gross: bool = True
    "True if the credit note items are given in gross-prices. This also changes the appereance of the credit note as prices are shown gross."
    # TODO Make this an environment-variable parameter
    overall_discount: Union[Unset, Discount] = UNSET
    "Apply an optional overall discount"
    _foot_text: Union[Unset, str] = UNSET
    "Internal cache of the foot text when caching credit note from SevDesk"
    ref_invoice: Union[int, Invoice] = UNSET
    "Reference to an invoice if booking-type is underachievment"
    accounting_type: Union[Unset, AccountingType] = UNSET
    "Accounting category/type if booking-type is accounting"
    tax_number: Union[Unset, str] = UNSET
    "Tax-Number of the receiving customer, necessary if booking-type is accounting"
    vat_number: Union[Unset, str] = UNSET
    "Optional VAT-Number of receiving customer"

    def __attrs_post_init__(self):
        if not self.tax_text:
            self.tax_text = f"Mehrwertssteuer {self.tax_rate}%"

        if not self.credit_note_date:
            self.credit_note_date = datetime.today().replace(microsecond=0)

        if not self.delivery_date:
            self.delivery_date = self.credit_note_date

        if self.booking_category == BookingCategory.UNDERACHIEVEMENT and isinstance(
            self.ref_invoice, Unset
        ):
            raise ValueError(
                "Booking category is UNDERACHIEVMENT but no invoice was given"
            )
        elif self.booking_category == BookingCategory.ACCOUNTING_TYPE:
            if isinstance(self.accounting_type, Unset) or isinstance(
                self.tax_number, Unset
            ):
                raise ValueError(
                    "Booking category is ACCOUNTING_TYPE but no accounting type or tax-number was given"
                )
        elif (
            self.booking_category == BookingCategory.PROVISION
            or self.booking_category == BookingCategory.ROYALTY_ASSIGNED
            or self.booking_category == BookingCategory.ROYALTY_UNASSIGNED
        ):
            raise ValueError(
                f"Booking category {self.booking_category} not implemented."
            )

    def _get_api_model(self, client: Client) -> CreateCreditNoteByFactoryJsonBody:
        if not self.contact_person:
            self.contact_person = SevDesk.user(client)

        if not self.credit_note_number:
            # Query the Credit Note Number only once
            response = get_next_credit_note_number.sync_detailed(
                client=client, credit_note_type="CN", use_next_number=False
            )
            SevDesk.raise_for_status(response, "getting next credit note number")

            self.credit_note_number = response.parsed.objects

        credit_note_model_contact = DocumentModelContact(self.customer.id)
        address = self.customer.get_invoice_address_string()
        address_country = UNSET

        if self.customer.invoice_address:
            static_country = self.customer.invoice_address._get_static_country(client)
            address_country = DocumentModelAddressCountry(id=static_country.id)

        credit_note_object = FactoryCreditNote(
            id=self.id,
            header=self.header,
            foot_text=self._foot_text,
            credit_note_number=self.credit_note_number,
            contact=credit_note_model_contact,
            address=address,
            address_country=address_country,
            status=self.status._get_api_model(client),
            credit_note_date=self.credit_note_date,
            delivery_date=self.delivery_date,
            small_settlement=self.small_settlement,
            contact_person=DocumentModelContactPerson(self.contact_person.id),
            tax_rate=self.tax_rate,
            tax_text=self.tax_text,
            customer_internal_note=self.reference,
            show_net=not self.gross,
            ref_src_invoice=CreditNoteRefSrcInvoice(id=self.ref_invoice.id)
            if self.ref_invoice
            else UNSET,
            accounting_type=CreditNoteAccountingType(id=self.accounting_type.id)
            if self.accounting_type
            else UNSET,
            booking_category=self.booking_category._get_api_model(client),
            tax_number=self.tax_number,
            vat_number=self.vat_number,
        )

        credit_note_pos = []
        item: LineItem
        for item in self.items:
            model = item._get_api_model(client, FactoryCreditNotePositionSave)
            credit_note_pos.append(model)

        discount_save = []
        if self.overall_discount:
            model = self.overall_discount._get_api_model(client, FactoryDiscountSave)
            discount_save.append(model)

        return CreateCreditNoteByFactoryJsonBody(
            credit_note=credit_note_object,
            credit_note_pos_save=credit_note_pos if credit_note_pos else None,
            credit_note_pos_delete=None,
            discount_save=discount_save if discount_save else None,
            discount_delete=None,
            take_default_address=False,
        )

    def _update_ids(self, response: CreateCreditNoteByFactoryResponse201):
        # Update IDs
        response: CreateCreditNoteByFactoryResponse201Objects
        response = response.parsed.objects
        self.id = int(response.credit_note.id)

        if self.items:
            local: CreditNotePosition
            cloud: CreditNotePosition
            for local, cloud in zip(self.items, response.credit_note_pos):
                if local.name != cloud.name:
                    raise RuntimeError("Order of lineitems does not match.")
                local.id = int(cloud.id)

        if self.overall_discount:
            overall_discount = response.discount[0]
            self.overall_discount.id = int(overall_discount.id)

    def update(self, client: Client):
        if not self.id:
            RuntimeError("Cannot update unknwon credit note - missing ID.")

        # The Factory Endpoint can be used to update an credit note
        response = create_credit_note_by_factory.sync_detailed(
            client=client, json_body=self._get_api_model(client)
        )
        SevDesk.raise_for_status(response, "update credit note by factory")
        self._update_ids(response)

    def create(self, client: Client):
        if self.id:
            RuntimeError("Cannot create an already known credit note - update instead?")

        response = create_credit_note_by_factory.sync_detailed(
            client=client, json_body=self._get_api_model(client)
        )
        SevDesk.raise_for_status(response, "creating credit note by factory")
        self._update_ids(response)

    def delete(self, client: Client):
        if not self.id:
            raise RuntimeError("Cannot delete unknwon credit note - missing ID.")

        response = delete_credit_note.sync_detailed(document_id=self.id, client=client)
        SevDesk.raise_for_status(response, "deleting an credit note")

    @classmethod
    def _from_model(cls, client: Client, model: FactoryCreditNote) -> CreditNote:
        # Query customer
        customer = Contact.get_by_id(client, model.contact.id)

        # Query Credit Note Positions
        response = get_credit_note_pos.sync_detailed(
            client=client,
            credit_noteobject_name="CreditNote",
            credit_noteid=model.id,
            limit=9999,
            embed="part,part.unity,unity",
        )
        SevDesk.raise_for_status(response, "getting credit note positions")

        items = []
        for line in response.parsed.objects:
            items.append(LineItem._from_model(client, line))

        # Query Overall Discount
        response = get_credit_note_discounts_by_id.sync_detailed(
            client=client, document_id=model.id
        )
        SevDesk.raise_for_status(response, "getting credit note discounts")

        overall_discount = UNSET
        if response.parsed.objects:
            overall_discount = Discount._from_model(client, response.parsed.objects[0])

        ref_invoice = UNSET
        if model.ref_src_invoice:
            ref_invoice = Invoice.get_by_id(client, model.ref_src_invoice.id)

        accounting_type = UNSET
        if model.accounting_type:
            accounting_type = AccountingType._get_by_id(
                client, model.accounting_type.id
            )

        return cls(
            customer=customer,
            header=model.header,
            reference=model.customer_internal_note,
            status=CreditNoteStatus(model.status),
            id=int(model.id),
            credit_note_date=model.credit_note_date,
            delivery_date=model.delivery_date,
            tax_rate=float(model.tax_rate),
            small_settlement=bool(int(model.small_settlement)),
            tax_text=model.tax_text,
            contact_person=SevUser(id=model.contact_person.id),
            credit_note_number=model.credit_note_number,
            gross=not bool(int(model.show_net)),
            foot_text=model.foot_text,
            items=items if items else UNSET,
            overall_discount=overall_discount,
            booking_category=BookingCategory(model.booking_category.value),
            ref_invoice=ref_invoice,
            tax_number=model.tax_number,
            vat_number=model.vat_number,
            accounting_type=accounting_type,
        )

    def download_pdf(self, client: Client) -> Pdf:
        """
        Download the credit note as PDF.
        Be careful - this will mark the credit note as send!
        """
        if not self.id:
            raise RuntimeError(
                "Cannot download pdf for unknwon credit note - missing ID!"
            )
        response = credit_note_get_pdf.sync_detailed(client=client, document_id=self.id)
        SevDesk.raise_for_status(response, "downloading credit note as PDF")

        pdf = response.parsed.objects

        return Pdf(
            filename=pdf.filename,
            base64_encoded=pdf.base_64_encoded,
            content=pdf.content,
        )

    def set_to_draft(self, client: Client):
        """
        If possible (credit note not enshrined), reset to draft-status
        """
        if not self.id:
            raise RuntimeError(
                "Cannot change status for unknown credit note - missing ID!"
            )

        response = credit_note_change_status.sync_detailed(
            document_id=self.id,
            client=client,
            json_body=CreditNoteChangeStatusJsonBody(
                value=CreditNoteChangeStatusJsonBodyValue.VALUE_1
            ),
        )

        SevDesk.raise_for_status(response, "change credit note status to draft")

    @classmethod
    def get_by_reference(
        cls, client: Client, reference: str
    ) -> Union[None, CreditNote]:
        """
        This Client makes using references (customer_interal_note) mandatory.
        For example, Shopify-Orders can be mapped to SevDesk Credit-Notes by using the Shopify (Legacy) ID.
        This allows to query credit notes by their reference.
        """
        response = get_credit_notes.sync_detailed(
            client=client, customer_internal_note=reference
        )
        SevDesk.raise_for_status(
            response, "getting credit note by reference (customer_internal_note)"
        )

        if not response.parsed.objects:
            return None

        credit_note_model = response.parsed.objects[0]
        return CreditNote._from_model(client, credit_note_model)


@attrs.define()
class Underachievment(CreditNote):
    """
    An underachievment linked to an invoice. Make sure to set ref_invoice
    when creating this type of credit note
    """

    booking_category: BookingCategory = BookingCategory.UNDERACHIEVEMENT


@attrs.define()
class AccountingNote(CreditNote):
    """
    An accounting type credit note typically used in internal use-cases
    (e.g. multi-purpose gift cards). Make sure to set accounting_type
    """

    booking_category: BookingCategory = BookingCategory.ACCOUNTING_TYPE
