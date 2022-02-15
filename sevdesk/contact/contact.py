from __future__ import annotations

import logging
from enum import Enum
from typing import Dict, Union
from unicodedata import category

import attrs
from cattr import UnstructureStrategy
from sevdesk.contact.address import AddressCategory

from sevdesk.contact.client.models.communication_way_model_type import (
    CommunicationWayModelType,
)


#
# OpenAPI SevDesk Client

from .. import Client
from ..common import ApiObject, ApiObjectCache, ApiObjectType, SevDesk, UNSET, Unset
from . import DeliveryAddress, InvoiceAddress, Email, Phone, CommunicationWayKey

from .client.models import ContactModelCategory, GetContactsDepth, ContactModel
from .client.api.contact import get_contacts, create_contact, update_contact


@attrs.define()
class Contact:
    """
    A Simplified Contact-Model allowing exactly one E-Mail, Phone, Delivery Address and Invoice Address
    This approach allows seamless integration with e.g. Shopify API
    """

    surename: str
    familyname: str
    customer_number: str
    category: ContactModelCategory
    email: Union[Unset, Email] = UNSET
    phone: Union[Unset, Phone] = UNSET
    delivery_address: Union[Unset, DeliveryAddress] = UNSET
    invoice_address: Union[Unset, InvoiceAddress] = UNSET
    id: Union[Unset, str] = UNSET

    def get_api_model(self, client: Client) -> ContactModel:
        return ContactModel(
            surename=self.surename,
            familyname=self.familyname,
            category=self.category,
            customer_number=self.customer_number,
        )

    def create(self, client: Client):
        response = create_contact.sync_detailed(
            client=client, json_body=self.get_api_model(client)
        )

        SevDesk.raise_for_status(
            response, f"creating contact for {self.surename} {self.familyname}"
        )

        # The newly created/existing contact object in SevDesk
        contact = response.parsed.objects
        self.id = contact.id

        if self.invoice_address:
            self.invoice_address.contact_id = self.id
            self.invoice_address.create(client)

        if self.delivery_address:
            self.delivery_address.contact_id = self.id
            self.delivery_address.create(client)

        if self.email:
            self.email.contact_id = self.id
            self.email.create(client)

        if self.phone:
            self.phone.contact_id = self.id
            self.phone.create(client)

    def update(self, client: Client, create: bool = True):
        if not self.id and create:
            return self.create(client)

        if not self.id:
            raise ValueError(
                f"SevDesk ID for contact is {self.surename} {self.familyname} missing. Cannot update unknown."
            )

        response = update_contact.sync_detailed(
            contact_id=self.id, client=client, json_body=self.get_api_model(client)
        )

        SevDesk.raise_for_status(
            response, f"updating contact for {self.surename} {self.familyname}"
        )

        if self.invoice_address:
            self.invoice_address.contact_id = self.id
            self.invoice_address.update(client)

        if self.delivery_address:
            self.delivery_address.contact_id = self.id
            self.delivery_address.update(client)

        if self.email:
            self.email.contact_id = self.id
            self.email.update(client)

        if self.phone:
            self.phone.contact_id = self.id
            self.phone.update(client)

    def delete(self, client: Client):
        pass

    @classmethod
    def get_by_customer_number(
        cls, client: Client, customer_number: str
    ) -> Union[Unset, Contact]:
        """
        This API Abstraction makes using customer numbers mandatory.
        For example, Shopify-Customers can be mapped to SevDesk Contacts by using their Shopify (Legacy) ID
        """
        response = get_contacts.sync_detailed(
            client=client,
            depth=GetContactsDepth.VALUE_1,
            customer_number=customer_number,
            embed=["addresses,adresses.country,communicationWays,parent"],
        )

        SevDesk.raise_for_status(
            response, f"get contact for customer number {customer_number}"
        )

        if not response.parsed.objects:
            return UNSET

        cache = ApiObjectCache(client=client)
        object = response.parsed.objects[0]

        # Addresses
        delivery_address = UNSET
        invoice_address = UNSET
        countries = cache.get(ApiObjectType.COUNTRY).sort_by_id()

        for address in object.addresses:
            category = AddressCategory.get_by_id(client, address.category.id)
            code = countries[address.country.id].code

            if category == AddressCategory.CATEGORY_DELIVERY_ADDRESS:
                if not delivery_address:
                    delivery_address = DeliveryAddress(
                        street=address.street,
                        zip_=address.zip_,
                        city=address.city,
                        id=address.id,
                        contact_id=object.id,
                        country_code=code,
                    )
                else:
                    raise ValueError(
                        "This Contact has more than one delivery address, unsupported behaviour."
                    )

            if category == AddressCategory.CATEGORY_INVOICE_ADDRESS:
                if not invoice_address:
                    invoice_address = DeliveryAddress(
                        street=address.street,
                        zip_=address.zip_,
                        city=address.city,
                        id=address.id,
                        contact_id=object.id,
                        country_code=code,
                    )
                else:
                    raise ValueError(
                        "This Contact has more than one invoice address, unsupported behaviour."
                    )

        # Communication-Ways
        email = UNSET
        phone = UNSET

        for communication_way in object.communication_ways:
            if communication_way.type == CommunicationWayModelType.EMAIL:
                if not email:
                    email = Email(
                        value=communication_way.value,
                        id=communication_way.id,
                        contact_id=object.id,
                        key=CommunicationWayKey.get_by_id(
                            client, communication_way.key.id
                        ),
                    )

                else:
                    raise ValueError(
                        "This Contact has more than one E-Mail, this is not unsupported behaviour."
                    )

            if communication_way.type == CommunicationWayModelType.PHONE:
                if not phone:
                    phone = Phone(
                        value=communication_way.value,
                        id=communication_way.id,
                        contact_id=object.id,
                        key=CommunicationWayKey.get_by_id(
                            client, communication_way.key.id
                        ),
                    )

                else:
                    raise ValueError(
                        "This Contact has more than one Phone-Number, unsupported behaviour."
                    )

        return cls(
            surename=object.surename,
            familyname=object.familyname,
            customer_number=object.customer_number,
            category=object.category,
            id=object.id,
            email=email,
            phone=phone,
            delivery_address=delivery_address,
            invoice_address=invoice_address,
        )


# A convinent class to access the SevDesk contact API
# The class implies some limitations to make updating/handling of contacts easier
# - A contact can only have one invoice address, shipping address, E-Mail and Phone-Number
# - The API exposes methods to conviniently use Shopify Webhooks (update and create)
class ContactApi:
    def __init__(self, client) -> None:
        self._client = client

        # Some Resources needed when working with the API, fetched once
        self.sevdesk = SevDesk(client=self._client)
        self.countries = self.sevdesk.countries()
        self.address_categories = self.sevdesk.contact_address_categories()
        self.communication_ways = self.sevdesk.communication_way_keys()

    def get_contact_by_customer_number(self, customer_number):
        # Get a contact including some additional information supported by this API client (addresses, communication-ways)
        response = get_contacts.sync_detailed(
            client=self._client,
            depth=GetContactsDepth.VALUE_1,
            customer_number=customer_number,
            embed=["addresses,adresses.country,communicationWays,parent"],
        )

        SevDesk.raise_for_status(
            response, f"get contact for customer number {customer_number}"
        )

        return response.parsed.objects[0]

    def add_address_to_contact(self, contact_id, address: Address):
        response = contact_add_address.sync_detailed(
            contact_id=contact_id,
            client=self._client,
            json_body=address.to_contact_add_address_json_body(
                countries=self.countries, address_categories=self.address_categories
            ),
        )

        return response

    def update_address(self, other, address: Address):
        response = update_contact_address.sync_detailed(
            client=self._client,
            contact_address_id=address.id,
            json_body=address.to_contact_address_from_other(
                countries=self.countries, other=other
            ),
        )
        return response

    def delete_address(self, address: Address):
        response = delete_contact_address.sync_detailed(
            client=self._client, contact_address_id=address.id
        )
        return response

    def create_customer(self, customer: Customer):
        response = create_contact.sync_detailed(
            client=self._client, json_body=customer.to_contact_model()
        )

        SevDesk.raise_for_status(
            response, f"creating contact for {customer.surename} {customer.familyname}"
        )

        # The newly created/existing contact object in SevDesk
        contact = response.parsed.objects

        # Create Adresses if given
        if not isinstance(customer.invoice_address, Unset):
            response = self.add_address_to_contact(contact.id, customer.invoice_address)
            SevDesk.raise_for_status(
                response,
                f"adding address for {customer.surename} {customer.familyname}",
            )

        if not isinstance(customer.delivery_address, Unset):
            response = self.add_address_to_contact(
                contact.id, customer.delivery_address
            )
            SevDesk.raise_for_status(
                response,
                f"adding address for {customer.surename} {customer.familyname}",
            )

        # TODO: Create communication objects if given

        if not isinstance(customer.email, Unset):
            create_communication_way.sync_detailed(
                client=self._client,
                json_body=customer.email.get_api_model(
                    contact.id, self.communication_ways
                ),
            )
            SevDesk.raise_for_status(
                response, f"adding email to {customer.surename} {customer.familyname}"
            )

        if not isinstance(customer.phone, Unset):
            create_communication_way.sync_detailed(
                client=self._client,
                json_body=customer.phone.get_api_model(
                    contact.id, self.communication_ways
                ),
            )
            SevDesk.raise_for_status(
                response, f"adding phone to {customer.surename} {customer.familyname}"
            )

        return contact

    def get_customer(self, customer: Customer):
        try:
            return self.get_contact_by_customer_number(customer.customer_number)
        except:
            return None

    def cpd_contact(self):
        cpd = Customer(
            surename="Shopify", familyname="Customer", customer_number="CPDCustomer"
        )

        response = self.get_customer(cpd)
        if response is None:
            response = self.create_customer(cpd)

        return response

    def update(self, customer: Customer, create: bool = True) -> Customer:
        # Check if customer exists within SevDesk
        contact = self.get_customer(customer)

        if contact is None and create:
            # Customer does not exist, create and return the customer object with added ID
            contact = self.create_customer(customer)

            customer.id = contact.id
            return contact

        elif contact is None:
            raise IOError(f"A customer with given id {customer.id} does not exist.")

        # Force-Update the actual contact
        response = update_contact.sync_detailed(
            client=self._client,
            contact_id=contact.id,
            json_body=customer.to_contact_model(),
        )

        SevDesk.raise_for_status(
            response, f"creating contact for {customer.surename} {customer.familyname}"
        )

        # Get Addresses to update and check update logic (only one invoice and one delivery address per contact)
        invoice_address = None
        delivery_address = None
        invoice_id = AddressType.get_id_for_address_type(
            self.address_categories, AddressType.CATEGORY_INVOICE_ADDRESS
        )
        delivery_id = AddressType.get_id_for_address_type(
            self.address_categories, AddressType.CATEGORY_DELIVERY_ADDRESS
        )

        for address in contact.addresses:
            if address.category.id == invoice_id:
                if invoice_address is None:
                    invoice_address = address
                else:
                    raise ValueError(
                        f"Only one Invoice Address per contact is supported. Failure in updating SevDesk customer with customer id {customer.customer_number}"
                    )
            elif address.category.id == delivery_id:
                if delivery_address is None:
                    delivery_address = address
                else:
                    raise ValueError(
                        f"Only one Invoice Address per contact is supported. Failure in updating SevDesk customer with customer id {customer.customer_number}"
                    )

        # create address
        if invoice_address is None and not isinstance(customer.invoice_address, Unset):
            response = self.add_address_to_contact(contact.id, customer.invoice_address)
            SevDesk.raise_for_status(
                response,
                f"adding address for {customer.surename} {customer.familyname}",
            )

        # Update
        elif invoice_address is not None and not isinstance(
            customer.invoice_address, Unset
        ):
            self.update_address(invoice_address, customer.invoice_address)
            SevDesk.raise_for_status(
                response,
                f"adding address for {customer.surename} {customer.familyname}",
            )

        # Delete
        elif invoice_address is not None and isinstance(
            customer.invoice_address, Unset
        ):
            self.delete_address(invoice_address)

        # Fetch latest version and return
        return self.get_customer(customer)


@attrs.define()
class Customer(Contact):
    category: ContactModelCategory = attrs.field(default=ContactModelCategory(id=3))
