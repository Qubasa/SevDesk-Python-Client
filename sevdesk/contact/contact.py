from __future__ import annotations

from typing import Union

import attrs
from sevdesk.contact.address import AddressCategory
from sevdesk.contact.client.models.communication_way_model_type import (
    CommunicationWayModelType,
)

from .. import Client
from ..common import UNSET, ApiObjectCache, ApiObjectType, SevDesk, Unset
from . import CommunicationWayKey, DeliveryAddress, Email, InvoiceAddress, Phone
from .client.api.contact import (
    create_contact,
    delete_contact,
    get_contacts,
    update_contact,
)
from .client.models import ContactModel, ContactModelCategory, GetContactsDepth


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
            self.invoice_address.parent = self
            self.invoice_address.create(client)

        if self.delivery_address:
            self.delivery_address.parent = self
            self.delivery_address.create(client)

        if self.email:
            self.email.parent = self
            self.email.create(client)

        if self.phone:
            self.phone.parent = self
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
            self.invoice_address.parent = self
            self.invoice_address.update(client)

        if self.delivery_address:
            self.delivery_address.parent = self
            self.delivery_address.update(client)

        if self.email:
            self.email.parent = self
            self.email.update(client)

        if self.phone:
            self.phone.parent = self
            self.phone.update(client)

    def delete(self, client: Client):
        """
        Delete contact and its properties
        """
        if self.invoice_address:
            self.invoice_address.delete(client)

        if self.delivery_address:
            self.delivery_address.delete(client)

        if self.email:
            self.email.delete(client)

        if self.phone:
            self.phone.delete(client)

        response = delete_contact.sync_detailed(contact_id=self.id, client=client)

        SevDesk.raise_for_status(
            response, f"deleting contact {self.surename} {self.familyname}"
        )

    @classmethod
    def get_by_customer_number(
        cls, client: Client, customer_number: str
    ) -> Union[None, Contact]:
        """
        This Client makes using customer numbers mandatory.
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
            return None

        cache = ApiObjectCache(client=client)
        object = response.parsed.objects[0]
        self = cls(
            surename=object.surename,
            familyname=object.familyname,
            customer_number=object.customer_number,
            category=object.category,
            id=object.id,
        )

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
                        parent=self,
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
                        parent=self,
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
                        parent=self,
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
                        parent=self,
                        key=CommunicationWayKey.get_by_id(
                            client, communication_way.key.id
                        ),
                    )

                else:
                    raise ValueError(
                        "This Contact has more than one Phone-Number, unsupported behaviour."
                    )

        self.email = email
        self.phone = phone
        self.delivery_address = delivery_address
        self.invoice_address = invoice_address

        return self


@attrs.define()
class Customer(Contact):
    category: ContactModelCategory = attrs.field(default=ContactModelCategory(id=3))
