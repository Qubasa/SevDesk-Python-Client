import os

from sevdesk import Client
from sevdesk.contact import Customer, Email, Phone, DeliveryAddress, InvoiceAddress
from sevdesk.common import Unset
from sevdesk.contact.communicationway import CommunicationWayKey


def test_get_customer_by_id():
    token = os.environ["SEVDESKTOKEN"]

    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)

    # A Test-Customer should already exist in SevDesk
    customer = Customer.get_by_customer_number(client, "1000")

    assert not isinstance(customer, Unset)


def test_customer():
    token = os.environ["SEVDESKTOKEN"]

    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)
    customer = Customer(
        surename="Slim",
        familyname="Shady",
        customer_number="1001",
        email=Email(value="slim.shady@test.mail"),
        delivery_address=DeliveryAddress(
            street="Slim-Shady-Street 1A",
            zip_="1010",
            city="Slim Shady Town",
            country_code="at",
        ),
        invoice_address=InvoiceAddress(
            street="Slim-Shady-Street 20",
            zip_="1020",
            city="Slim Shady Village",
            country_code="at",
        ),
    )

    customer.create(client)
    assert not isinstance(customer.id, Unset)
    assert not isinstance(customer.email.id, Unset)
    assert not isinstance(customer.delivery_address.id, Unset)
    assert not isinstance(customer.invoice_address.id, Unset)

    # Test updating a customer
    customer.surename = "changed"
    customer.delivery_address.street = "changed"
    customer.email.value = "changed"
    customer.phone = Phone(
        value="0123 456789", key=CommunicationWayKey.COMM_WAY_KEY_INVOICE_ADDRESS
    )

    customer.update(client)
    cloud = Customer.get_by_customer_number(client, "1001")

    assert not isinstance(cloud, Unset)
    assert customer.surename == cloud.surename
    assert customer.delivery_address.street == cloud.delivery_address.street
    assert customer.email.value == cloud.email.value
    assert customer.phone.value == cloud.phone.value

    # TODO: Test Delete
    # TODO: Test Update/Delete
