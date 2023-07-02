from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.book_invoice_json_body_type import BookInvoiceJsonBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.book_invoice_json_body_check_account import (
        BookInvoiceJsonBodyCheckAccount,
    )
    from ..models.book_invoice_json_body_check_account_transaction import (
        BookInvoiceJsonBodyCheckAccountTransaction,
    )


T = TypeVar("T", bound="BookInvoiceJsonBody")


@attr.s(auto_attribs=True)
class BookInvoiceJsonBody:
    """
    Attributes:
        amount (float): Amount which should be booked. Can also be a partial amount.
        date (int): The booking date. Most likely the current date.
        type (BookInvoiceJsonBodyType): Define a type for the booking. The following type abbreviations are available
            (abbreviation <-> meaning). N <-> Normal booking / partial booking, CB <-> Reduced amount due to discount
            (skonto), CF <-> Reduced/Higher amount due to currency fluctuations, O <-> Reduced/Higher amount due to other
            reasons, OF <-> Higher amount due to reminder charges, MTC <-> Reduced amount due to the monetary traffic costs
        check_account (BookInvoiceJsonBodyCheckAccount): The check account on which should be booked.
        check_account_transaction (Union[Unset, BookInvoiceJsonBodyCheckAccountTransaction]): The check account
            transaction on which should be booked. The transaction will be linked to the invoice.
        create_feed (Union[Unset, bool]): Determines if a feed is created for the booking process.
    """

    amount: float
    date: int
    type: BookInvoiceJsonBodyType
    check_account: "BookInvoiceJsonBodyCheckAccount"
    check_account_transaction: Union[
        Unset, "BookInvoiceJsonBodyCheckAccountTransaction"
    ] = UNSET
    create_feed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        date = self.date
        type = self.type.value

        check_account = self.check_account.to_dict()

        check_account_transaction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.check_account_transaction, Unset):
            check_account_transaction = self.check_account_transaction.to_dict()

        create_feed = self.create_feed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
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
        from ..models.book_invoice_json_body_check_account import (
            BookInvoiceJsonBodyCheckAccount,
        )
        from ..models.book_invoice_json_body_check_account_transaction import (
            BookInvoiceJsonBodyCheckAccountTransaction,
        )

        d = src_dict.copy()
        amount = d.pop("amount")

        date = d.pop("date")

        type = BookInvoiceJsonBodyType(d.pop("type"))

        check_account = BookInvoiceJsonBodyCheckAccount.from_dict(d.pop("checkAccount"))

        _check_account_transaction = d.pop("checkAccountTransaction", UNSET)
        check_account_transaction: Union[
            Unset, BookInvoiceJsonBodyCheckAccountTransaction
        ]
        if isinstance(_check_account_transaction, Unset):
            check_account_transaction = UNSET
        else:
            check_account_transaction = (
                BookInvoiceJsonBodyCheckAccountTransaction.from_dict(
                    _check_account_transaction
                )
            )

        create_feed = d.pop("createFeed", UNSET)

        book_invoice_json_body = cls(
            amount=amount,
            date=date,
            type=type,
            check_account=check_account,
            check_account_transaction=check_account_transaction,
            create_feed=create_feed,
        )

        book_invoice_json_body.additional_properties = d
        return book_invoice_json_body

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
