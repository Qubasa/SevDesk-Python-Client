from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.factory_credit_note import FactoryCreditNote
from ..models.factory_credit_note_position_delete import FactoryCreditNotePositionDelete
from ..models.factory_credit_note_position_save import FactoryCreditNotePositionSave
from ..models.factory_discount_delete import FactoryDiscountDelete
from ..models.factory_discount_save import FactoryDiscountSave
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCreditNoteByFactoryJsonBody")


@attr.s(auto_attribs=True)
class CreateCreditNoteByFactoryJsonBody:
    """
    Attributes:
        credit_note (FactoryCreditNote):
        credit_note_pos_save (Optional[List[FactoryCreditNotePositionSave]]): The credit note positions you want to
            create. If you don't have any, set to null.
        credit_note_pos_delete (Optional[List[FactoryCreditNotePositionDelete]]): The credit note positions you want to
            delete. If you don't have any, set to null.
        discount_save (Optional[List[FactoryDiscountSave]]): The discounts you want to create. If you don't have any,
            set to null.
        discount_delete (Optional[List[FactoryDiscountDelete]]): The discounts you want to delete. If you don't have
            any, set to null.
        take_default_address (Union[Unset, bool]): Defines if the address of the supplied contact is automatically
            filled into the credit-note. Default: True.
        for_cash_register (Union[Unset, bool]): If the Credit Note is for the cash register change to true, otherwise
            leave at false. Default: True.
    """

    credit_note: FactoryCreditNote
    credit_note_pos_save: Optional[List[FactoryCreditNotePositionSave]]
    credit_note_pos_delete: Optional[List[FactoryCreditNotePositionDelete]]
    discount_save: Optional[List[FactoryDiscountSave]]
    discount_delete: Optional[List[FactoryDiscountDelete]]
    take_default_address: Union[Unset, bool] = True
    for_cash_register: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_note = self.credit_note.to_dict()

        if self.credit_note_pos_save is None:
            credit_note_pos_save = None
        else:
            credit_note_pos_save = []
            for credit_note_pos_save_item_data in self.credit_note_pos_save:
                credit_note_pos_save_item = credit_note_pos_save_item_data.to_dict()

                credit_note_pos_save.append(credit_note_pos_save_item)

        if self.credit_note_pos_delete is None:
            credit_note_pos_delete = None
        else:
            credit_note_pos_delete = []
            for credit_note_pos_delete_item_data in self.credit_note_pos_delete:
                credit_note_pos_delete_item = credit_note_pos_delete_item_data.to_dict()

                credit_note_pos_delete.append(credit_note_pos_delete_item)

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
        for_cash_register = self.for_cash_register

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditNote": credit_note,
                "creditNotePosSave": credit_note_pos_save,
                "creditNotePosDelete": credit_note_pos_delete,
                "discountSave": discount_save,
                "discountDelete": discount_delete,
            }
        )
        if take_default_address is not UNSET:
            field_dict["takeDefaultAddress"] = take_default_address
        if for_cash_register is not UNSET:
            field_dict["forCashRegister"] = for_cash_register

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credit_note = FactoryCreditNote.from_dict(d.pop("creditNote"))

        credit_note_pos_save = []
        _credit_note_pos_save = d.pop("creditNotePosSave")
        for credit_note_pos_save_item_data in _credit_note_pos_save or []:
            credit_note_pos_save_item = FactoryCreditNotePositionSave.from_dict(
                credit_note_pos_save_item_data
            )

            credit_note_pos_save.append(credit_note_pos_save_item)

        credit_note_pos_delete = []
        _credit_note_pos_delete = d.pop("creditNotePosDelete")
        for credit_note_pos_delete_item_data in _credit_note_pos_delete or []:
            credit_note_pos_delete_item = FactoryCreditNotePositionDelete.from_dict(
                credit_note_pos_delete_item_data
            )

            credit_note_pos_delete.append(credit_note_pos_delete_item)

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

        for_cash_register = d.pop("forCashRegister", UNSET)

        create_credit_note_by_factory_json_body = cls(
            credit_note=credit_note,
            credit_note_pos_save=credit_note_pos_save,
            credit_note_pos_delete=credit_note_pos_delete,
            discount_save=discount_save,
            discount_delete=discount_delete,
            take_default_address=take_default_address,
            for_cash_register=for_cash_register,
        )

        create_credit_note_by_factory_json_body.additional_properties = d
        return create_credit_note_by_factory_json_body

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
