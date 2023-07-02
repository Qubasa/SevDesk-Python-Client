from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.factory_discount_delete import FactoryDiscountDelete
    from ..models.factory_discount_save import FactoryDiscountSave
    from ..models.factory_invoice import FactoryInvoice
    from ..models.factory_invoice_position_delete import FactoryInvoicePositionDelete
    from ..models.factory_invoice_position_save import FactoryInvoicePositionSave


T = TypeVar("T", bound="CreateInvoiceByFactoryJsonBody")


@attr.s(auto_attribs=True)
class CreateInvoiceByFactoryJsonBody:
    """
    Attributes:
        invoice (FactoryInvoice):
        invoice_pos_save (Optional[List['FactoryInvoicePositionSave']]): The invoice positions you want to create. If
            you don't have any, set to null.
        invoice_pos_delete (Optional[List['FactoryInvoicePositionDelete']]): The invoice positions you want to delete.
            If you don't have any, set to null.
        discount_save (Optional[List['FactoryDiscountSave']]): The discounts you want to create. If you don't have any,
            set to null.
        discount_delete (Optional[List['FactoryDiscountDelete']]): The discounts you want to delete. If you don't have
            any, set to null.
        take_default_address (Union[Unset, bool]): Defines if the address of the supplied contact is automatically
            filled into the invoice. Default: True.
    """

    invoice: "FactoryInvoice"
    invoice_pos_save: Optional[List["FactoryInvoicePositionSave"]]
    invoice_pos_delete: Optional[List["FactoryInvoicePositionDelete"]]
    discount_save: Optional[List["FactoryDiscountSave"]]
    discount_delete: Optional[List["FactoryDiscountDelete"]]
    take_default_address: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice = self.invoice.to_dict()

        if self.invoice_pos_save is None:
            invoice_pos_save = None
        else:
            invoice_pos_save = []
            for invoice_pos_save_item_data in self.invoice_pos_save:
                invoice_pos_save_item = invoice_pos_save_item_data.to_dict()

                invoice_pos_save.append(invoice_pos_save_item)

        if self.invoice_pos_delete is None:
            invoice_pos_delete = None
        else:
            invoice_pos_delete = []
            for invoice_pos_delete_item_data in self.invoice_pos_delete:
                invoice_pos_delete_item = invoice_pos_delete_item_data.to_dict()

                invoice_pos_delete.append(invoice_pos_delete_item)

        if self.discount_save is None:
            discount_save = None
        else:
            discount_save = []
            for discount_save_item_data in self.discount_save:
                discount_save_item = discount_save_item_data.to_dict()

                discount_save.append(discount_save_item)

        if self.discount_delete is None:
            discount_delete = None
        else:
            discount_delete = []
            for discount_delete_item_data in self.discount_delete:
                discount_delete_item = discount_delete_item_data.to_dict()

                discount_delete.append(discount_delete_item)

        take_default_address = self.take_default_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice": invoice,
                "invoicePosSave": invoice_pos_save,
                "invoicePosDelete": invoice_pos_delete,
                "discountSave": discount_save,
                "discountDelete": discount_delete,
            }
        )
        if take_default_address is not UNSET:
            field_dict["takeDefaultAddress"] = take_default_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.factory_discount_delete import FactoryDiscountDelete
        from ..models.factory_discount_save import FactoryDiscountSave
        from ..models.factory_invoice import FactoryInvoice
        from ..models.factory_invoice_position_delete import (
            FactoryInvoicePositionDelete,
        )
        from ..models.factory_invoice_position_save import FactoryInvoicePositionSave

        d = src_dict.copy()
        invoice = FactoryInvoice.from_dict(d.pop("invoice"))

        invoice_pos_save = []
        _invoice_pos_save = d.pop("invoicePosSave")
        for invoice_pos_save_item_data in _invoice_pos_save or []:
            invoice_pos_save_item = FactoryInvoicePositionSave.from_dict(
                invoice_pos_save_item_data
            )

            invoice_pos_save.append(invoice_pos_save_item)

        invoice_pos_delete = []
        _invoice_pos_delete = d.pop("invoicePosDelete")
        for invoice_pos_delete_item_data in _invoice_pos_delete or []:
            invoice_pos_delete_item = FactoryInvoicePositionDelete.from_dict(
                invoice_pos_delete_item_data
            )

            invoice_pos_delete.append(invoice_pos_delete_item)

        discount_save = []
        _discount_save = d.pop("discountSave")
        for discount_save_item_data in _discount_save or []:
            discount_save_item = FactoryDiscountSave.from_dict(discount_save_item_data)

            discount_save.append(discount_save_item)

        discount_delete = []
        _discount_delete = d.pop("discountDelete")
        for discount_delete_item_data in _discount_delete or []:
            discount_delete_item = FactoryDiscountDelete.from_dict(
                discount_delete_item_data
            )

            discount_delete.append(discount_delete_item)

        take_default_address = d.pop("takeDefaultAddress", UNSET)

        create_invoice_by_factory_json_body = cls(
            invoice=invoice,
            invoice_pos_save=invoice_pos_save,
            invoice_pos_delete=invoice_pos_delete,
            discount_save=discount_save,
            discount_delete=discount_delete,
            take_default_address=take_default_address,
        )

        create_invoice_by_factory_json_body.additional_properties = d
        return create_invoice_by_factory_json_body

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
