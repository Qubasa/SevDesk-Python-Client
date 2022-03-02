from __future__ import annotations

from typing import Union

import attrs

from .. import UNSET, Client, Unset
from ..client.api.contact import (
    create_contact,
    delete_contact,
    get_contact_by_id,
    get_contacts,
    update_contact,
)
from ..client.models import ContactModel, ContactModelCategory, GetContactsDepth
from ..client.models.communication_way_model_type import CommunicationWayModelType
from ..common import ApiObjectCache, ApiObjectType, SevDesk
from .address import AddressCategory, DeliveryAddress, InvoiceAddress
from .communicationway import CommunicationWayKey, Email, Phone


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

    def _get_api_model(self, client: Client) -> ContactModel:
        return ContactModel(
            surename=self.surename,
            familyname=self.familyname,
            category=self.category,
            customer_number=self.customer_number,
        )

    def create(self, client: Client):
        response = create_contact.sync_detailed(
            client=client, json_body=self._get_api_model(client)
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
            contact_id=self.id, client=client, json_body=self._get_api_model(client)
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

    def get_invoice_address_string(self) -> str:
        address = []
        name = ""
        if self.surename:
            name += f"{self.surename} "
        if self.familyname:
            name += f"{self.familyname}"
        if name:
            address.append(name)

        if self.invoice_address:
            if self.invoice_address.street:
                address.append(f"{self.invoice_address.street}")

            city = ""
            if self.invoice_address.zip_:
                city += f"{self.invoice_address.zip_} "
            if self.invoice_address.city:
                city += f"{self.invoice_address.city}"
            if city:
                address.append(city)

        return "\n".join(address)

    @classmethod
    def _from_contact_model(
        cls, client: Client, contact_model: ContactModel
    ) -> Contact:
        cache = ApiObjectCache(client=client)

        self = cls(
            surename=contact_model.surename,
            familyname=contact_model.familyname,
            customer_number=contact_model.customer_number,
            category=contact_model.category,
            id=contact_model.id,
        )

        # Addresses
        delivery_address = UNSET
        invoice_address = UNSET
        countries = cache.get(ApiObjectType.COUNTRY).sort_by_id()

        for address in contact_model.addresses:
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
                    invoice_address = InvoiceAddress(
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

        for communication_way in contact_model.communication_ways:
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

    @classmethod
    def get_by_id(cls, client: Client, id: int) -> Union[None, Contact]:
        """
        Use the SevDesk ID to get a specific contact
        """
        response = get_contact_by_id.sync_detailed(
            contact_id=id,
            client=client,
            embed=["addresses,adresses.country,communicationWays,parent"],
        )

        SevDesk.raise_for_status(response, "getting contact by ID")
        if not response.parsed.objects:
            return None

        contact_model = response.parsed.objects[0]
        return Contact._from_contact_model(client, contact_model)

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

        contact_model = response.parsed.objects[0]
        return Contact._from_contact_model(client, contact_model)


@attrs.define()
class Customer(Contact):
    category: ContactModelCategory = attrs.field(default=ContactModelCategory(id=3))
