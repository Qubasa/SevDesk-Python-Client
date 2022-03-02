import os

from sevdesk import Client, Unset
from sevdesk.contact import Customer
from sevdesk.accounting import (
    Invoice,
    InvoiceStatus,
    Transaction,
    LineItem,
    Discount,
    Unity,
    Underachievment,
    CreditNoteStatus,
    AccountingCategories,
    AccountingNote,
)


def test_accounting_type_credit_note():
    token = os.environ["SEVDESKTOKEN"]
    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)
    reference = "FFFFFFFFFFF"

    customer = Customer.get_by_customer_number(client, "1000")
    categories = AccountingCategories.get(client)
    accounting_type = categories.find("Sonstiges.Spenden")

    accounting_note = AccountingNote(
        status=CreditNoteStatus.DRAFT,
        customer=customer,
        header="Interne Gutschrift zu Auftrag #1000",
        reference=reference,
        items=[
            LineItem(
                name="Test-Item 1",
                quantity=1,
                price=100,
                tax=20,
                unity=Unity.PIECE,
                discount=Discount(value=25, percentage=False),
            )
        ],
        accounting_type=accounting_type,
        tax_number="N/A-INTERNAL",
    )

    accounting_note.create(client)
    cloud = AccountingNote.get_by_reference(client, reference)
    assert cloud.accounting_type.id == accounting_type.id

    accounting_note.delete(client)
    cloud = AccountingNote.get_by_reference(client, reference)
    assert cloud is None


def test_underachievment_credit_note():
    token = os.environ["SEVDESKTOKEN"]
    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)
    reference = "FFFFFFFFFFF"

    # Append Invoice to Test-Customer
    customer = Customer.get_by_customer_number(client, "1000")
    invoice = Invoice.get_by_reference(client, reference)

    if not invoice:
        # Instantiate the invoice and create
        invoice = Invoice(
            status=InvoiceStatus.DRAFT,
            customer=customer,
            header="Rechnung zu Auftrag #1000",
            reference=reference,
            items=[
                LineItem(
                    name="Test-Item 1",
                    quantity=1,
                    price=100,
                    tax=20,
                    unity=Unity.PIECE,
                    discount=Discount(value=25, percentage=False),
                ),
                LineItem(
                    name="Test-Item 2",
                    text="A very testable item",
                    quantity=5,
                    price=99.99,
                    tax=20,
                    unity=Unity.CUBIC_METER,
                    discount=Discount(value=5, percentage=True),
                ),
            ],
            # Transactions are shown in the foot-text of the invoice
            transactions=[
                Transaction(gateway="Voucher", amount=50, voucher=True),
                Transaction(gateway="Credit-Card", amount=45),
                Transaction(gateway="Cash", amount=25),
            ],
            # The Invoice-Model allows to apply an overall discount
            overall_discount=Discount(value=5, percentage=True),
        )
        invoice.create(client)

    # Download a PDF (which will mark invoice as send)
    invoice.download_pdf(client)

    # Now, create an underachievment corresponding to the invoice
    underachievment = Underachievment(
        status=CreditNoteStatus.DRAFT,
        customer=customer,
        header="Gutschrift zu Auftrag #1000",
        reference=reference,
        items=[
            LineItem(
                name="Test-Item 1",
                quantity=1,
                price=100,
                tax=20,
                unity=Unity.PIECE,
                discount=Discount(value=25, percentage=False),
            )
        ],
        overall_discount=Discount(value=5, percentage=True),
        ref_invoice=invoice,
    )
    underachievment.create(client)

    assert not isinstance(underachievment.id, Unset)
    assert not isinstance(underachievment.items[0].id, Unset)
    assert not isinstance(underachievment.overall_discount.id, Unset)

    # Update the underachievment by changing some properties
    underachievment.items.append(
        LineItem(name="Test-Item 2", quantity=1, price=49.99, tax=20)
    )
    underachievment.header = "Rechnung zu Auftrag #1000-Update"
    underachievment.items[0].name = "Test-Item 1 - Update"
    underachievment.update(client)

    # Get the incoive using its reference
    cloud = Underachievment.get_by_reference(client, reference)

    # Make sure an update calling on the cloud object does not change properties in SevDesk
    cloud.update(client)
    cloud = Underachievment.get_by_reference(client, reference)

    assert underachievment.customer.id == cloud.customer.id
    assert underachievment.customer.surename == cloud.customer.surename
    assert underachievment.customer.familyname == cloud.customer.familyname
    assert underachievment.header == cloud.header
    assert underachievment.reference == cloud.reference
    assert underachievment.status == cloud.status
    assert underachievment.id == cloud.id
    assert underachievment.small_settlement == cloud.small_settlement
    assert underachievment.tax_rate == cloud.tax_rate
    assert underachievment.tax_text == cloud.tax_text
    assert underachievment.contact_person.id == cloud.contact_person.id
    assert underachievment.gross == cloud.gross
    assert underachievment.overall_discount.id == cloud.overall_discount.id
    assert underachievment.overall_discount.text == cloud.overall_discount.text
    assert underachievment.overall_discount.value == cloud.overall_discount.value
    assert (
        underachievment.overall_discount.percentage == cloud.overall_discount.percentage
    )

    local_item: LineItem
    cloud_item: LineItem
    for local_item, cloud_item in zip(underachievment.items, cloud.items):
        assert local_item.id == cloud_item.id
        assert local_item.name == cloud_item.name
        assert local_item.price == cloud_item.price
        assert local_item.quantity == cloud_item.quantity
        assert local_item.tax == cloud_item.tax
        assert local_item.text == cloud_item.text
        assert local_item.unity == cloud_item.unity
        if local_item.discount:
            assert local_item.discount.value == cloud_item.discount.value
            assert local_item.discount.percentage == cloud_item.discount.percentage
            assert local_item.discount.text == cloud_item.discount.text
            assert local_item.discount.id == cloud_item.discount.id
        else:
            assert isinstance(cloud_item.discount, Unset)

    assert underachievment.ref_invoice.id == cloud.ref_invoice.id

    # Download a PDF (which will mark invoice as send)
    underachievment.download_pdf(client)

    # Reset to draft
    underachievment.set_to_draft(client)
    invoice.set_to_draft(client)

    # Delete invoice and underachievment
    underachievment.delete(client)
    invoice.delete(client)
