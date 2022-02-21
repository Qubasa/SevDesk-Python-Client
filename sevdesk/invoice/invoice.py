from datetime import datetime
from enum import Enum
from typing import List, Union
import attrs

from .. import Client
from ..common import UNSET, SevUser, Unset
from ..common.sevdesk import SevDesk
from ..contact import Contact
from .client.api.invoice import create_invoice_by_factory, get_next_invoice_number
from .client.models import (
    CreateInvoiceByFactoryJsonBody,
    InvoiceModelContact,
    InvoiceModelStatus,
    SaveInvoiceInvoiceObject,
    InvoiceModelContactPerson,
    SaveInvoiceDiscountSave,
)
from .discount import Discount
from .lineitem import LineItem
from .transaction import Transaction


class InvoiceStatus(Enum):
    DRAFT = InvoiceModelStatus.VALUE_1
    OPEN = InvoiceModelStatus.VALUE_2
    PAYED = InvoiceModelStatus.VALUE_3

    def get_api_model(self, client: Client) -> InvoiceModelStatus:
        return self.value


@attrs.define()
class Invoice:
    """
    A simplified helper to create invoices in SevDesk.
    The class is optimised for Shopify, but covers the most common use-cases.
    To simplify book-keeping all transaction gateways (e.g. a customer pays with partly with credit card and cash or uses a voucher)
    are shown on the Invoice. When creating the invoice, it will be marked as sent but not as payed.
    """

    contact: Contact
    "The contact the invoice belongs to."
    ordercode: str
    "The ordercode is used to generate a meaningful invoice header"
    reference: Union[Unset, str] = UNSET
    "The reference allows the API to filter for a specific invoice. A Shopify Client could use the reference to store the Shopify API ID. If not set, the reference will be equal to the ordercode"
    status: InvoiceStatus = InvoiceStatus.DRAFT
    "Invoice-Status"
    items: Union[Unset, List[LineItem]] = UNSET
    "Invoice-Items"
    transactions: Union[Unset, List[Transaction]] = UNSET
    "Payment transacitons. Will be added to the footer of the invoice."
    id: Union[Unset, str] = UNSET
    "Internal parameter of the invoice ID. Will be set when creted."
    invoice_date: Union[Unset, datetime] = UNSET
    "Invoice timestamp. If not set, datetime.now() will be called on initialisation of the invoice object."
    delivery_date: Union[Unset, datetime] = UNSET
    "Delivery timestamp. If not set, invoice_date will be used as delivery_date."
    small_settlement: bool = False
    "Defines if the client uses the small settlement scheme. If yes, the invoice must not contain any vat."
    # TODO Make this an environment-variable parameter
    tax_rate: float = 20.0
    "Default tax-rate, overwritten by the line item."
    # TODO Make an environment-variable parameter
    tax_text: Union[Unset, str] = UNSET
    "Default tax-text, will be automatically set to Mehrwertssteuer {tax_rate}%"
    contact_person: Union[Unset, SevUser] = UNSET
    "The contact person. If not given, the SevUser corresponding to the API-Token will be used"
    invoice_number: Union[Unset, str] = UNSET
    "The invoice number. If not set, the next number will be queried from SevDesk on calling the create function."
    gross: bool = True
    "True if the invoice items are given in gross-prices. This also changes the appereance of the invoice as prices are shown gross."
    # TODO Make this an environment-variable parameter
    overall_discount: Union[Unset, Discount] = UNSET
    "Apply an optional overall discount"

    def __attrs_post_init__(self):
        if not self.tax_text:
            self.tax_text = f"Mehrwertssteuer {self.tax_rate}%"

        if not self.invoice_date:
            self.invoice_date = datetime.now()

        if not self.delivery_date:
            self.delivery_date = self.invoice_date

        if not self.reference:
            self.reference = self.ordercode

    def get_api_model(self, client: Client) -> CreateInvoiceByFactoryJsonBody:
        if not self.contact_person:
            self.contact_person = SevDesk.user(client)

        if not self.invoice_number:
            response = get_next_invoice_number.sync_detailed(
                client=client, invoice_type="RE", use_next_number=False
            )
            SevDesk.raise_for_status(response, "getting next invoice number")

            self.invoice_number = response.parsed.objects

        header = f"Rechnung zu Auftrag {self.ordercode}"

        foot_text = ""
        if self.transactions:
            foot_text += "Zahlungsgateways:"
            foot_text += "<ul>"
            for transaction in self.transactions:
                foot_text += f"<li>{transaction.gateway}: {transaction.amount} EUR</li>"
            foot_text += "</ul>"

        invoice_model_contact = InvoiceModelContact(self.contact.id)
        invoice_object = SaveInvoiceInvoiceObject(
            header=header,
            foot_text=foot_text,
            invoice_number=self.invoice_number,
            contact=invoice_model_contact,
            status=self.status.get_api_model(client),
            invoice_date=self.invoice_date,
            delivery_date=self.delivery_date,
            small_settlement=self.small_settlement,
            contact_person=InvoiceModelContactPerson(self.contact_person.id),
            tax_rate=self.tax_rate,
            tax_text=self.tax_text,
            customer_internal_note=self.reference,
            show_net=not self.gross,
        )

        invoice_pos = []
        for item in self.items:
            invoice_pos.append(item.get_api_model(client))

        discount_save = []
        if self.overall_discount:
            discount_save.append(
                SaveInvoiceDiscountSave(
                    discount=True,
                    text=self.overall_discount.text,
                    percentage=self.overall_discount.percentage,
                    value=self.overall_discount.value,
                )
            )

        return CreateInvoiceByFactoryJsonBody(
            invoice=invoice_object,
            invoice_pos_save=invoice_pos if invoice_pos else None,
            invoice_pos_delete=None,
            discount_save=discount_save if discount_save else None,
            discount_delete=None,
        )

    @classmethod
    def get_by_reference(cls, client: Client):
        """
        Invoices created by the API use the customer_interal_note as a reference.
        This allows to query a specific invoice by its reference.
        """
        # TODO use query parameter customerIntenalNote={note}
        pass

    def create(self, client: Client):
        response = create_invoice_by_factory.sync_detailed(
            client=client, json_body=self.get_api_model(client)
        )
        SevDesk.raise_for_status(response, "creating invoice by factory")
