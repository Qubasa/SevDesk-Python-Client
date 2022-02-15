# Typing
from __future__ import annotations
from audioop import add
from typing import Union
from enum import Enum
import attrs

from .. import Client
from ..common import ApiObject, ApiObjectCache, ApiObjectType, SevDesk, UNSET, Unset

from .client.models import (
    ContactAddress,
    ContactAddressCategory,
    ContactAddressCountry,
    ContactAddressContact,
    ContactAddAddressJsonBody,
)
from .client.api.contact_address import (
    create_contact_address,
    delete_contact_address,
    update_contact_address,
)
from sevdesk.contact.client.api import contact_address


class AddressCategory(str, Enum):
    CATEGORY_WORK = "CATEGORY_WORK"
    CATEGORY_INVOICE_ADDRESS = "CATEGORY_INVOICE_ADDRESS"
    CATEGORY_DELIVERY_ADDRESS = "CATEGORY_DELIVERY_ADDRESS"

    def get_api_model(self, client: Client) -> ContactAddressCategory:
        cache = ApiObjectCache(client=client)
        item: ApiObject = cache.get(ApiObjectType.ADDRESS_CATEGORIES)[self]

        return ContactAddressCategory(item.id, "Category")

    @staticmethod
    def get_by_id(client: Client, id: str) -> AddressCategory:
        cache = ApiObjectCache(client=client)
        keys = cache.get(ApiObjectType.ADDRESS_CATEGORIES).sort_by_id()
        key = keys[id]

        return AddressCategory[key.translationCode]


@attrs.define()
class Address:
    street: str
    zip_: str
    city: str
    country_code: str
    category: AddressCategory
    id: Union[Unset, str] = UNSET
    contact_id: Union[Unset, str] = UNSET

    def get_api_model(self, client: Client) -> ContactAddress:
        cache = ApiObjectCache(client=client)
        country: ApiObject = cache.get(ApiObjectType.COUNTRY)[self.country_code.lower()]

        address = ContactAddress(
            contact=ContactAddressContact(self.contact_id),
            country=ContactAddressCountry(id=country.id),
            zip_=self.zip_,
            city=self.city,
            street=self.street,
            category=self.category.get_api_model(client),
        )

        if self.id:
            address.id = self.id

        return address

    def create(self, client: Client):
        """
        Create the address by appending it to the given client
        """
        if not self.contact_id:
            raise ValueError("Cannt create Address without a contact-id.")

        response = create_contact_address.sync_detailed(
            client=client, json_body=self.get_api_model(client)
        )

        SevDesk.raise_for_status(response, "creating address")
        self.id = response.parsed.objects.id

    def update(self, client: Client, create: bool = True):
        """
        Updating a communication way
        """
        if not self.id and create:
            return self.create(client)

        if not self.id:
            raise ValueError("Address ID not set, cannot update unknown.")

        response = update_contact_address.sync_detailed(
            self.id, client=client, json_body=self.get_api_model(client)
        )
        SevDesk.raise_for_status(response, "updating address")

    def delete(self, client: Client):
        """
        Deleting the given communication way by its ID
        """
        if not self.id:
            raise ValueError("Communication-Way-ID not set, cannot delete unknown.")

        response = delete_contact_address.sync_detailed(self.id, client=client)
        SevDesk.raise_for_status(response, "deleting address")


@attrs.define()
class InvoiceAddress(Address):
    category: AddressCategory = attrs.field(
        default=AddressCategory.CATEGORY_INVOICE_ADDRESS
    )


@attrs.define()
class DeliveryAddress(Address):
    category: AddressCategory = attrs.field(
        default=AddressCategory.CATEGORY_DELIVERY_ADDRESS
    )
