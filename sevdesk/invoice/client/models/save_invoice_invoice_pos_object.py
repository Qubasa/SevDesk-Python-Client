import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.invoice_position_model_invoice import InvoicePositionModelInvoice
from ..models.invoice_position_model_part import InvoicePositionModelPart
from ..models.invoice_position_model_sev_client import InvoicePositionModelSevClient
from ..models.invoice_position_model_unity import InvoicePositionModelUnity
from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveInvoiceInvoicePosObject")


@attr.s(auto_attribs=True)
class SaveInvoiceInvoicePosObject:
    """
    Attributes:
        invoice (InvoicePositionModelInvoice): The invoice to which the position belongs.
        unity (InvoicePositionModelUnity): The unit in which the positions part is measured
        tax_rate (float): Tax rate of the position. Example: 19.
        map_all (bool):  Default: True.
        id (Union[Unset, int]): The invoice position id
        object_name (Union[Unset, str]): The invoice position object name Default: 'InvoicePos'.
        create (Union[Unset, datetime.datetime]): Date of invoice position creation
        update (Union[Unset, datetime.datetime]): Date of last invoice position update
        part (Union[Unset, InvoicePositionModelPart]): Part from your inventory which is used in the position.
        quantity (Union[Unset, None, float]): Quantity of the article/part Example: 1.
        price (Union[Unset, None, float]): Price of the article/part. Is either gross or net, depending on the sevDesk
            account setting. Example: 100.
        name (Union[Unset, None, float]): Name of the article/part. Example: Dragonglass.
        priority (Union[Unset, int]): Priority of the position. Default: 100.
        sev_client (Union[Unset, InvoicePositionModelSevClient]): Client to which invoice position belongs. Will be
            filled automatically
        position_number (Union[Unset, None, int]): Position number of your position. Can be used to order multiple
            positions.
        text (Union[Unset, None, str]): A text describing your position.
        discount (Union[Unset, None, float]): An optional discount of the position.
        temporary (Union[Unset, None, bool]): Defines if the position is temporary
        sum_net (Union[Unset, None, float]): Net sum of the position
        sum_gross (Union[Unset, None, float]): Gross sum of the position
        sum_discount (Union[Unset, None, float]): Discount sum of the position
        sum_tax (Union[Unset, float]): Tax sum of the position
        sum_net_accounting (Union[Unset, None, float]): Net accounting sum of the position
        sum_tax_accounting (Union[Unset, None, float]): Tax accounting sum of the position
        sum_gross_accounting (Union[Unset, None, float]): Gross accounting sum of the position
        price_net (Union[Unset, None, float]): Net price of the part
        price_gross (Union[Unset, None, float]): Gross price of the part Example: 100.
        price_tax (Union[Unset, None, float]): Tax on the price of the part
    """

    invoice: InvoicePositionModelInvoice
    unity: InvoicePositionModelUnity
    tax_rate: float
    map_all: bool = True
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = "InvoicePos"
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    part: Union[Unset, InvoicePositionModelPart] = UNSET
    quantity: Union[Unset, None, float] = UNSET
    price: Union[Unset, None, float] = UNSET
    name: Union[Unset, None, float] = UNSET
    priority: Union[Unset, int] = 100
    sev_client: Union[Unset, InvoicePositionModelSevClient] = UNSET
    position_number: Union[Unset, None, int] = UNSET
    text: Union[Unset, None, str] = UNSET
    discount: Union[Unset, None, float] = UNSET
    temporary: Union[Unset, None, bool] = UNSET
    sum_net: Union[Unset, None, float] = UNSET
    sum_gross: Union[Unset, None, float] = UNSET
    sum_discount: Union[Unset, None, float] = UNSET
    sum_tax: Union[Unset, float] = UNSET
    sum_net_accounting: Union[Unset, None, float] = UNSET
    sum_tax_accounting: Union[Unset, None, float] = UNSET
    sum_gross_accounting: Union[Unset, None, float] = UNSET
    price_net: Union[Unset, None, float] = UNSET
    price_gross: Union[Unset, None, float] = UNSET
    price_tax: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice = self.invoice.to_dict()

        unity = self.unity.to_dict()

        tax_rate = self.tax_rate
        map_all = self.map_all
        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.part, Unset):
            part = self.part.to_dict()

        quantity = self.quantity
        price = self.price
        name = self.name
        priority = self.priority
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        position_number = self.position_number
        text = self.text
        discount = self.discount
        temporary = self.temporary
        sum_net = self.sum_net
        sum_gross = self.sum_gross
        sum_discount = self.sum_discount
        sum_tax = self.sum_tax
        sum_net_accounting = self.sum_net_accounting
        sum_tax_accounting = self.sum_tax_accounting
        sum_gross_accounting = self.sum_gross_accounting
        price_net = self.price_net
        price_gross = self.price_gross
        price_tax = self.price_tax

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice": invoice,
                "unity": unity,
                "taxRate": tax_rate,
                "mapAll": map_all,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if part is not UNSET:
            field_dict["part"] = part
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price is not UNSET:
            field_dict["price"] = price
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if position_number is not UNSET:
            field_dict["positionNumber"] = position_number
        if text is not UNSET:
            field_dict["text"] = text
        if discount is not UNSET:
            field_dict["discount"] = discount
        if temporary is not UNSET:
            field_dict["temporary"] = temporary
        if sum_net is not UNSET:
            field_dict["sumNet"] = sum_net
        if sum_gross is not UNSET:
            field_dict["sumGross"] = sum_gross
        if sum_discount is not UNSET:
            field_dict["sumDiscount"] = sum_discount
        if sum_tax is not UNSET:
            field_dict["sumTax"] = sum_tax
        if sum_net_accounting is not UNSET:
            field_dict["sumNetAccounting"] = sum_net_accounting
        if sum_tax_accounting is not UNSET:
            field_dict["sumTaxAccounting"] = sum_tax_accounting
        if sum_gross_accounting is not UNSET:
            field_dict["sumGrossAccounting"] = sum_gross_accounting
        if price_net is not UNSET:
            field_dict["priceNet"] = price_net
        if price_gross is not UNSET:
            field_dict["priceGross"] = price_gross
        if price_tax is not UNSET:
            field_dict["priceTax"] = price_tax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice = InvoicePositionModelInvoice.from_dict(d.pop("invoice"))

        unity = InvoicePositionModelUnity.from_dict(d.pop("unity"))

        tax_rate = d.pop("taxRate")

        map_all = d.pop("mapAll")

        id = d.pop("id", UNSET)

        object_name = d.pop("objectName", UNSET)

        _create = d.pop("create", UNSET)
        create: Union[Unset, datetime.datetime]
        if isinstance(_create, Unset):
            create = UNSET
        else:
            create = isoparse(_create)

        _update = d.pop("update", UNSET)
        update: Union[Unset, datetime.datetime]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = isoparse(_update)

        _part = d.pop("part", UNSET)
        part: Union[Unset, InvoicePositionModelPart]
        if isinstance(_part, Unset):
            part = UNSET
        else:
            part = InvoicePositionModelPart.from_dict(_part)

        quantity = d.pop("quantity", UNSET)

        price = d.pop("price", UNSET)

        name = d.pop("name", UNSET)

        priority = d.pop("priority", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, InvoicePositionModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = InvoicePositionModelSevClient.from_dict(_sev_client)

        position_number = d.pop("positionNumber", UNSET)

        text = d.pop("text", UNSET)

        discount = d.pop("discount", UNSET)

        temporary = d.pop("temporary", UNSET)

        sum_net = d.pop("sumNet", UNSET)

        sum_gross = d.pop("sumGross", UNSET)

        sum_discount = d.pop("sumDiscount", UNSET)

        sum_tax = d.pop("sumTax", UNSET)

        sum_net_accounting = d.pop("sumNetAccounting", UNSET)

        sum_tax_accounting = d.pop("sumTaxAccounting", UNSET)

        sum_gross_accounting = d.pop("sumGrossAccounting", UNSET)

        price_net = d.pop("priceNet", UNSET)

        price_gross = d.pop("priceGross", UNSET)

        price_tax = d.pop("priceTax", UNSET)

        save_invoice_invoice_pos_object = cls(
            invoice=invoice,
            unity=unity,
            tax_rate=tax_rate,
            map_all=map_all,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            part=part,
            quantity=quantity,
            price=price,
            name=name,
            priority=priority,
            sev_client=sev_client,
            position_number=position_number,
            text=text,
            discount=discount,
            temporary=temporary,
            sum_net=sum_net,
            sum_gross=sum_gross,
            sum_discount=sum_discount,
            sum_tax=sum_tax,
            sum_net_accounting=sum_net_accounting,
            sum_tax_accounting=sum_tax_accounting,
            sum_gross_accounting=sum_gross_accounting,
            price_net=price_net,
            price_gross=price_gross,
            price_tax=price_tax,
        )

        save_invoice_invoice_pos_object.additional_properties = d
        return save_invoice_invoice_pos_object

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
