from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.invoice_model import InvoiceModel
from ..models.invoice_position_model import InvoicePositionModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInvoiceByFactoryResponse201ObjectsItem")


@attr.s(auto_attribs=True)
class CreateInvoiceByFactoryResponse201ObjectsItem:
    """
    Attributes:
        invoice (Union[Unset, InvoiceModel]): Invoice model
        invoice_pos (Union[Unset, None, List[InvoicePositionModel]]): The created invoice positions
    """

    invoice: Union[Unset, InvoiceModel] = UNSET
    invoice_pos: Union[Unset, None, List[InvoicePositionModel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice, Unset):
            invoice = self.invoice.to_dict()

        invoice_pos: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoice_pos, Unset):
            if self.invoice_pos is None:
                invoice_pos = None
            else:
                invoice_pos = []
                for invoice_pos_item_data in self.invoice_pos:
                    invoice_pos_item = invoice_pos_item_data.to_dict()

                    invoice_pos.append(invoice_pos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if invoice_pos is not UNSET:
            field_dict["invoicePos"] = invoice_pos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _invoice = d.pop("invoice", UNSET)
        invoice: Union[Unset, InvoiceModel]
        if isinstance(_invoice, Unset):
            invoice = UNSET
        else:
            invoice = InvoiceModel.from_dict(_invoice)

        invoice_pos = []
        _invoice_pos = d.pop("invoicePos", UNSET)
        for invoice_pos_item_data in _invoice_pos or []:
            invoice_pos_item = InvoicePositionModel.from_dict(invoice_pos_item_data)

            invoice_pos.append(invoice_pos_item)

        create_invoice_by_factory_response_201_objects_item = cls(
            invoice=invoice,
            invoice_pos=invoice_pos,
        )

        create_invoice_by_factory_response_201_objects_item.additional_properties = d
        return create_invoice_by_factory_response_201_objects_item

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
