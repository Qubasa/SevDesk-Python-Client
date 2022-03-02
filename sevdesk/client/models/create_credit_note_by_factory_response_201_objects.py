from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credit_note import CreditNote
from ..models.credit_note_position import CreditNotePosition
from ..models.discount_position_model import DiscountPositionModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCreditNoteByFactoryResponse201Objects")


@attr.s(auto_attribs=True)
class CreateCreditNoteByFactoryResponse201Objects:
    """
    Attributes:
        credit_note (Union[Unset, CreditNote]):
        credit_note_pos (Union[Unset, None, List[CreditNotePosition]]): The created credit note positions
        discount (Union[Unset, None, List[DiscountPositionModel]]): The created credit note discounts
    """

    credit_note: Union[Unset, CreditNote] = UNSET
    credit_note_pos: Union[Unset, None, List[CreditNotePosition]] = UNSET
    discount: Union[Unset, None, List[DiscountPositionModel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_note: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_note, Unset):
            credit_note = self.credit_note.to_dict()

        credit_note_pos: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credit_note_pos, Unset):
            if self.credit_note_pos is None:
                credit_note_pos = None
            else:
                credit_note_pos = []
                for credit_note_pos_item_data in self.credit_note_pos:
                    credit_note_pos_item = credit_note_pos_item_data.to_dict()

                    credit_note_pos.append(credit_note_pos_item)

        discount: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.discount, Unset):
            if self.discount is None:
                discount = None
            else:
                discount = []
                for discount_item_data in self.discount:
                    discount_item = discount_item_data.to_dict()

                    discount.append(discount_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_note is not UNSET:
            field_dict["creditNote"] = credit_note
        if credit_note_pos is not UNSET:
            field_dict["creditNotePos"] = credit_note_pos
        if discount is not UNSET:
            field_dict["discount"] = discount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _credit_note = d.pop("creditNote", UNSET)
        credit_note: Union[Unset, CreditNote]
        if isinstance(_credit_note, Unset):
            credit_note = UNSET
        else:
            credit_note = CreditNote.from_dict(_credit_note)

        credit_note_pos = []
        _credit_note_pos = d.pop("creditNotePos", UNSET)
        for credit_note_pos_item_data in _credit_note_pos or []:
            credit_note_pos_item = CreditNotePosition.from_dict(
                credit_note_pos_item_data
            )

            credit_note_pos.append(credit_note_pos_item)

        discount = []
        _discount = d.pop("discount", UNSET)
        for discount_item_data in _discount or []:
            discount_item = DiscountPositionModel.from_dict(discount_item_data)

            discount.append(discount_item)

        create_credit_note_by_factory_response_201_objects = cls(
            credit_note=credit_note,
            credit_note_pos=credit_note_pos,
            discount=discount,
        )

        create_credit_note_by_factory_response_201_objects.additional_properties = d
        return create_credit_note_by_factory_response_201_objects

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
