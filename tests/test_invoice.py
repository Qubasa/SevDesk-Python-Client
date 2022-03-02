import os

from sevdesk import Client, Unset
from sevdesk.contact import Customer
from sevdesk.accounting import (
    Invoice,
    InvoiceStatus,
    Transaction,
    Discount,
    LineItem,
    Unity,
)


def test_invoice():
    token = os.environ["SEVDESKTOKEN"]
    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)
    reference = "FFFFFFFFFFF"

    # Append Invoice to Test-Customer
    customer = Customer.get_by_customer_number(client, "1000")

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

    assert not isinstance(invoice.id, Unset)
    assert not isinstance(invoice.items[0].id, Unset)
    assert not isinstance(invoice.items[1].id, Unset)
    assert not isinstance(invoice.overall_discount.id, Unset)

    # Update the invoice by changing some properties
    invoice.items.append(LineItem(name="Test-Item 3", quantity=1, price=49.99, tax=20))
    invoice.header = "Rechnung zu Auftrag #1000-Update"
    invoice.items[0].name = "Test-Item 1 - Update"
    invoice.update(client)

    # Get the incoive using its reference
    cloud = Invoice.get_by_reference(client, reference)

    # Make sure an update calling on the cloud object does not change properties in SevDesk
    cloud.update(client)
    cloud = Invoice.get_by_reference(client, reference)

    assert invoice.customer.id == cloud.customer.id
    assert invoice.customer.surename == cloud.customer.surename
    assert invoice.customer.familyname == cloud.customer.familyname
    assert invoice.header == cloud.header
    assert invoice.reference == cloud.reference
    assert invoice.status == cloud.status
    assert invoice.id == cloud.id
    # assert invoice.invoice_date == cloud.invoice_date
    # assert invoice.delivery_date == cloud.delivery_date
    assert invoice.small_settlement == cloud.small_settlement
    assert invoice.tax_rate == cloud.tax_rate
    assert invoice.tax_text == cloud.tax_text
    assert invoice.contact_person.id == cloud.contact_person.id
    assert invoice.invoice_number == cloud.invoice_number
    assert invoice.gross == cloud.gross
    assert invoice.overall_discount.id == cloud.overall_discount.id
    assert invoice.overall_discount.text == cloud.overall_discount.text
    assert invoice.overall_discount.value == cloud.overall_discount.value
    assert invoice.overall_discount.percentage == cloud.overall_discount.percentage

    local_item: LineItem
    cloud_item: LineItem
    for local_item, cloud_item in zip(invoice.items, cloud.items):
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
    assert isinstance(cloud.transactions, Unset)

    # Download a PDF (which will mark invoice as send)
    invoice.download_pdf(client)

    # Reset to draft (This only works if SevDesk does not automatically enshrine invoices - refer to SevDesk Settings)
    invoice.set_to_draft(client)

    # Delete the draft-invoice
    invoice.delete(client)
    cloud = Invoice.get_by_reference(client, reference)
    assert cloud is None
