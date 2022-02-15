from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DeprecatedBookInvoiceJsonBodyCheckAccountTransaction")


@attr.s(auto_attribs=True)
class DeprecatedBookInvoiceJsonBodyCheckAccountTransaction:
    """The check account transaction on which should be booked.<br>
                                        The transaction will be linked to the invoice.

    Attributes:
        id (int): The id of the check account transaction on which should be booked.
        object_name (str): Internal object name which is 'CheckAccountTransaction'. Example: CheckAccountTransaction.
    """

    id: int
    object_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "objectName": object_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_name = d.pop("objectName")

        deprecated_book_invoice_json_body_check_account_transaction = cls(
            id=id,
            object_name=object_name,
        )

        deprecated_book_invoice_json_body_check_account_transaction.additional_properties = (
            d
        )
        return deprecated_book_invoice_json_body_check_account_transaction

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
