from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Union

import attrs

from .. import UNSET, Client, Unset
from ..client.api.invoice import (
    create_invoice_by_factory,
    delete_invoice,
    get_invoice_by_id,
    get_invoices,
    get_next_invoice_number,
    invoice_change_status,
    invoice_get_pdf,
)
from ..client.api.invoice_discounts import get_invoice_discounts_by_id
from ..client.api.invoice_pos import get_invoice_pos
from ..client.models import (
    CreateInvoiceByFactoryJsonBody,
    CreateInvoiceByFactoryResponse201,
    DocumentModelAddressCountry,
    DocumentModelContact,
    DocumentModelContactPerson,
    DocumentModelStatus,
    DocumentModelTaxType,
    FactoryDiscountSave,
    FactoryInvoice,
    FactoryInvoicePositionSave,
    InvoiceChangeStatusJsonBody,
    InvoiceChangeStatusJsonBodyValue,
)
from ..common import SevDesk, SevUser
from ..contact import Contact
from .discount import Discount
from .lineitem import LineItem
from .pdf import Pdf
from .transaction import Transaction


class InvoiceStatus(Enum):
    DRAFT = DocumentModelStatus.VALUE_1
    OPEN = DocumentModelStatus.VALUE_2
    PAYED = DocumentModelStatus.VALUE_3

    def _get_api_model(self, client: Client) -> DocumentModelStatus:
        return self.value


@attrs.define()
class Invoice:
    """
    A simplified helper to create invoices in SevDesk.
    The class is optimised for Shopify, but covers the most common use-cases.

    To simplify book-keeping all transaction gateways are shown on the Invoice.
    When creating the invoice, it will be marked as sent but not as payed.
    """

    customer: Contact = attrs.field(on_setattr=attrs.setters.frozen)
    "The customer the invoice belongs to. After the invoice is created, make sure to not change the customer anymore."
    header: str
    "The invoice header, e.g. 'Rechnung zu Auftrag #1000'"
    reference: Union[Unset, str] = attrs.field(on_setattr=attrs.setters.frozen)
    "The reference allows the API to filter for a specific invoice."
    "A Shopify Client could use the reference to store the Shopify API ID"
    status: InvoiceStatus = InvoiceStatus.DRAFT
    "Invoice-Status"
    head_text: Union[Unset, str] = UNSET
    "The head text"
    items: Union[Unset, List[LineItem]] = UNSET
    "Invoice-Items"
    transactions: Union[Unset, List[Transaction]] = UNSET
    "Payment transacitons. Will be added to the footer of the invoice."
    id: Union[Unset, str] = UNSET
    "Internal parameter of the invoice ID. Will be set when creted."
    invoice_date: Union[Unset, datetime] = UNSET
    "Invoice timestamp. If not set, datetime.now() will be called on initialisation of the invoice object."
    delivery_date: Union[Unset, datetime] = UNSET
    "Delivery date until timestamp"
    delivery_date_until: Union[Unset, None, datetime] = UNSET
    "Delivery timestamp. If not set, invoice_date will be used as delivery_date."
    small_settlement: bool = False
    "Defines if the client uses the small settlement scheme. If yes, the invoice must not contain any vat."
    # TODO Make this an environment-variable parameter
    tax_rate: float = 20.0
    "Default tax-rate, overwritten by the line item."
    # TODO Make an environment-variable parameter
    tax_text: Union[Unset, str] = UNSET
    "Default tax-text, will be automatically set to Mehrwertssteuer {tax_rate}%"
    tax_type: Union[Unset, DocumentModelTaxType] = UNSET
    "TODO"
    contact_person: Union[Unset, SevUser] = UNSET
    "The contact person. If not given, the SevUser corresponding to the API-Token will be used"
    invoice_number: Union[Unset, str] = UNSET
    "The invoice number. If not set, the next number will be queried from SevDesk on calling the create function."
    gross: bool = True
    "True if the invoice items are given in gross-prices. This also changes the appereance of the invoice as prices are shown gross."
    # TODO Make this an environment-variable parameter
    overall_discount: Union[Unset, Discount] = UNSET
    "Apply an optional overall discount"
    _foot_text: Union[Unset, str] = UNSET
    "Internal cache of the foot text when caching invoice from SevDesk"
    _address: Union[Unset, str] = UNSET
    "Internal cache of the address text when caching invoice from SevDesk"

    def __attrs_post_init__(self):
        if not self.tax_text:
            self.tax_text = f"Mehrwertssteuer {self.tax_rate}%"

        if not self.invoice_date:
            self.invoice_date = datetime.today().replace(microsecond=0)

        if not self.delivery_date:
            self.delivery_date = self.invoice_date

    def _get_api_model(self, client: Client) -> CreateInvoiceByFactoryJsonBody:
        if not self.contact_person:
            self.contact_person = SevDesk.user(client)

        if not self.invoice_number:
            # Query the Invoice-Number only once
            response = get_next_invoice_number.sync_detailed(
                client=client, invoice_type="RE", use_next_number=False
            )
            SevDesk.raise_for_status(response, "getting next invoice number")

            self.invoice_number = response.parsed.objects

        if self.transactions:
            self._foot_text = ""
            self._foot_text += "Zahlungsgateways:"
            self._foot_text += "<ul>"

            transaction: Transaction
            for transaction in self.transactions:
                self._foot_text += (
                    f"<li>{transaction.gateway}: {transaction.amount} EUR</li>"
                )
            self._foot_text += "</ul>"

        invoice_model_contact = DocumentModelContact(self.customer.id)
        address = self.customer.get_invoice_address_string()

        address_country = UNSET

        if self.customer.invoice_address:
            static_country = self.customer.invoice_address._get_static_country(client)
            address_country = DocumentModelAddressCountry(id=static_country.id)

        invoice_object = FactoryInvoice(
            id=self.id,
            header=self.header,
            head_text=self.head_text,
            foot_text=self._foot_text,
            invoice_number=self.invoice_number,
            contact=invoice_model_contact,
            address=address,
            address_country=address_country,
            status=self.status._get_api_model(client),
            invoice_date=self.invoice_date,
            delivery_date=self.delivery_date,
            delivery_date_until=self.delivery_date_until,
            small_settlement=self.small_settlement,
            contact_person=DocumentModelContactPerson(self.contact_person.id),
            tax_rate=self.tax_rate,
            tax_text=self.tax_text,
            tax_type=self.tax_type,
            customer_internal_note=self.reference,
            show_net=not self.gross,
        )

        invoice_pos = []
        item: LineItem
        for item in self.items:
            model = item._get_api_model(client, FactoryInvoicePositionSave)
            invoice_pos.append(model)

        discount_save = []
        if self.overall_discount:
            discount_save.append(
                self.overall_discount._get_api_model(client, FactoryDiscountSave)
            )

        return CreateInvoiceByFactoryJsonBody(
            invoice=invoice_object,
            invoice_pos_save=invoice_pos if invoice_pos else None,
            invoice_pos_delete=None,
            discount_save=discount_save if discount_save else None,
            discount_delete=None,
            take_default_address=False,
        )

    def _update_ids(self, response: CreateInvoiceByFactoryResponse201):
        # Update IDs
        response = response.parsed.objects
        self.id = int(response.invoice.id)

        if self.items:
            for local, cloud in zip(self.items, response.invoice_pos):
                if local.name != cloud.name:
                    raise RuntimeError("Order of lineitems does not match.")
                local.id = int(cloud.id)

        if self.overall_discount:
            overall_discount = response.discount[0]
            self.overall_discount.id = int(overall_discount.id)

    def update(self, client: Client):
        if not self.id:
            RuntimeError("Cannot update unknwon invoice - missing ID.")

        # The Factory Endpoint can be used to update an invoice
        response = create_invoice_by_factory.sync_detailed(
            client=client, json_body=self._get_api_model(client)
        )
        SevDesk.raise_for_status(response, "creating invoice by factory")
        self._update_ids(response)

    def create(self, client: Client):
        if self.id:
            RuntimeError("Cannot create an already known invoice - update instead?")

        response = create_invoice_by_factory.sync_detailed(
            client=client, json_body=self._get_api_model(client)
        )
        SevDesk.raise_for_status(response, "creating invoice by factory")
        self._update_ids(response)

    def delete(self, client: Client):
        if not self.id:
            raise RuntimeError("Cannot delete unknwon invoice - missing ID.")

        response = delete_invoice.sync_detailed(document_id=self.id, client=client)
        SevDesk.raise_for_status(response, "deleting an invoice")

    @classmethod
    def _from_model(cls, client: Client, model: FactoryInvoice) -> Invoice:
        # Query customer
        customer = Contact.get_by_id(client, model.contact.id)

        # Query Invoice Positions
        response = get_invoice_pos.sync_detailed(
            client=client,
            invoiceobject_name="Invoice",
            invoiceid=model.id,
            limit=9999,
            embed="part,part.unity,unity",
        )
        SevDesk.raise_for_status(response, "getting invoice positions")

        items = []
        for line in response.parsed.objects:
            items.append(LineItem._from_model(client, line))

        # Query Overall Discount
        response = get_invoice_discounts_by_id.sync_detailed(
            client=client, document_id=model.id
        )
        SevDesk.raise_for_status(response, "getting invoice discounts")

        overall_discount = UNSET
        if response.parsed.objects:
            overall_discount = Discount._from_model(client, response.parsed.objects[0])

        return cls(
            customer=customer,
            header=model.header,
            reference=model.customer_internal_note,
            status=InvoiceStatus(model.status),
            id=int(model.id),
            invoice_date=model.invoice_date,
            delivery_date=model.delivery_date,
            small_settlement=bool(int(model.small_settlement)),
            tax_rate=float(model.tax_rate),
            tax_text=model.tax_text,
            contact_person=SevUser(id=model.contact_person.id),
            invoice_number=model.invoice_number,
            gross=not bool(int(model.show_net)),
            foot_text=model.foot_text,
            items=items if items else UNSET,
            overall_discount=overall_discount,
            address=model.address,
        )

    def download_pdf(self, client: Client) -> Pdf:
        """
        Download the invoice as PDF.
        Be careful - this will mark the invoice as send!
        """
        if not self.id:
            raise RuntimeError("Cannot download pdf for unknwon invoice - missing ID!")
        response = invoice_get_pdf.sync_detailed(client=client, document_id=self.id)
        SevDesk.raise_for_status(response, "downloading invoice as PDF")

        pdf = response.parsed.objects

        return Pdf(
            filename=pdf.filename,
            base64_encoded=pdf.base_64_encoded,
            content=pdf.content,
        )

    def set_to_draft(self, client: Client):
        """
        If possible (invoice not enshrined), reset to draft-status
        """
        if not self.id:
            raise RuntimeError("Cannot change status for unknown invoice - missing ID!")

        response = invoice_change_status.sync_detailed(
            document_id=self.id,
            client=client,
            json_body=InvoiceChangeStatusJsonBody(
                value=InvoiceChangeStatusJsonBodyValue.VALUE_1
            ),
        )

        SevDesk.raise_for_status(response, "change invoice status to draft")

    @classmethod
    def get_by_reference(cls, client: Client, reference: str) -> Union[None, Invoice]:
        """
        This Client makes using references (customer_interal_note) mandatory.
        For example, Shopify-Orders can be mapped to SevDesk Invoices by using the Shopify (Legacy) ID.
        This allows to query invoices by their reference.

        Be aware: Fetching data from SevDesk will not fully restore the invoice in python.
        The Transactions will be missing!

        However, you can still set new transactions to update an invoice.
        """
        response = get_invoices.sync_detailed(
            client=client, customer_internal_note=reference
        )
        SevDesk.raise_for_status(
            response, "getting invoice by reference (customer_internal_note)"
        )

        if not response.parsed.objects:
            return None

        invoice_model = response.parsed.objects[0]
        return Invoice._from_model(client, invoice_model)

    @classmethod
    def get_by_id(cls, client: Client, id: int) -> Union[None, Invoice]:
        response = get_invoice_by_id.sync_detailed(client=client, document_id=id)
        SevDesk.raise_for_status(response, "getting invoice by id")

        if not response.parsed.objects:
            return None

        invoice_model = response.parsed.objects[0]
        return Invoice._from_model(client, invoice_model)
