from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deprecated_book_invoice_json_body_check_account import (
    DeprecatedBookInvoiceJsonBodyCheckAccount,
)
from ..models.deprecated_book_invoice_json_body_check_account_transaction import (
    DeprecatedBookInvoiceJsonBodyCheckAccountTransaction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeprecatedBookInvoiceJsonBody")


@attr.s(auto_attribs=True)
class DeprecatedBookInvoiceJsonBody:
    """
    Attributes:
        ammount (float): Amount which should be booked. Can also be a partial amount.
        date (int): The booking date. Most likely the current date.
        type (str): Define a type for the booking.<br>
                 The following type abbreviations are available (abbreviation <-> meaning).<br>
                 <ul>
                    <li>N <-> Normal booking / partial booking</li>
                    <li>CB <-> Reduced amount due to discount (skonto)</li>
                    <li>CF <-> Reduced/Higher amount due to currency fluctuations</li>
                    <li>O <-> Reduced/Higher amount due to other reasons</li>
                    <li>OF <-> Higher amount due to reminder charges</li>
                    <li>MTC <-> Reduced amount due to the monetary traffic costs</li>
                 </ul>
        check_account (DeprecatedBookInvoiceJsonBodyCheckAccount): The check account on which should be booked.
        check_account_transaction (Union[Unset, DeprecatedBookInvoiceJsonBodyCheckAccountTransaction]): The check
            account transaction on which should be booked.<br>
                                                    The transaction will be linked to the invoice.
        create_feed (Union[Unset, bool]): Determines if a feed is created for the booking process.
    """

    ammount: float
    date: int
    type: str
    check_account: DeprecatedBookInvoiceJsonBodyCheckAccount
    check_account_transaction: Union[
        Unset, DeprecatedBookInvoiceJsonBodyCheckAccountTransaction
    ] = UNSET
    create_feed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ammount = self.ammount
        date = self.date
        type = self.type
        check_account = self.check_account.to_dict()

        check_account_transaction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.check_account_transaction, Unset):
            check_account_transaction = self.check_account_transaction.to_dict()

        create_feed = self.create_feed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ammount": ammount,
                "date": date,
                "type": type,
                "checkAccount": check_account,
            }
        )
        if check_account_transaction is not UNSET:
            field_dict["checkAccountTransaction"] = check_account_transaction
        if create_feed is not UNSET:
            field_dict["createFeed"] = create_feed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ammount = d.pop("ammount")

        date = d.pop("date")

        type = d.pop("type")

        check_account = DeprecatedBookInvoiceJsonBodyCheckAccount.from_dict(
            d.pop("checkAccount")
        )

        _check_account_transaction = d.pop("checkAccountTransaction", UNSET)
        check_account_transaction: Union[
            Unset, DeprecatedBookInvoiceJsonBodyCheckAccountTransaction
        ]
        if isinstance(_check_account_transaction, Unset):
            check_account_transaction = UNSET
        else:
            check_account_transaction = (
                DeprecatedBookInvoiceJsonBodyCheckAccountTransaction.from_dict(
                    _check_account_transaction
                )
            )

        create_feed = d.pop("createFeed", UNSET)

        deprecated_book_invoice_json_body = cls(
            ammount=ammount,
            date=date,
            type=type,
            check_account=check_account,
            check_account_transaction=check_account_transaction,
            create_feed=create_feed,
        )

        deprecated_book_invoice_json_body.additional_properties = d
        return deprecated_book_invoice_json_body

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
