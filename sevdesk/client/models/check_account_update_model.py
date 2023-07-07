from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.check_account_update_model_default_account import (
    CheckAccountUpdateModelDefaultAccount,
)
from ..models.check_account_update_model_import_type import (
    CheckAccountUpdateModelImportType,
)
from ..models.check_account_update_model_status import CheckAccountUpdateModelStatus
from ..models.check_account_update_model_type import CheckAccountUpdateModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckAccountUpdateModel")


@attr.s(auto_attribs=True)
class CheckAccountUpdateModel:
    """CheckAccount model. Responsible for the payment accounts.

    Attributes:
        name (Union[Unset, str]): Name of the check account Example: Iron Bank.
        type (Union[Unset, CheckAccountUpdateModelType]): The type of the check account. Account with a CSV or MT940
            import are regarded as online.<br>
                 Apart from that, created check accounts over the API need to be offline, as online accounts with an active
            connection
                 to a bank application can not be managed over the API. Example: online.
        import_type (Union[Unset, None, CheckAccountUpdateModelImportType]): Import type. Transactions can be imported
            by this method on the check account. Example: CSV.
        currency (Union[Unset, str]): The currency of the check account. Example: EUR.
        default_account (Union[Unset, CheckAccountUpdateModelDefaultAccount]): Defines if this check account is the
            default account. Default: CheckAccountUpdateModelDefaultAccount.VALUE_0.
        status (Union[Unset, CheckAccountUpdateModelStatus]): Status of the check account. 0 <-> Archived - 100 <->
            Active Default: CheckAccountUpdateModelStatus.VALUE_100.
        auto_map_transactions (Union[Unset, None, int]): Defines if transactions on this account are automatically
            mapped to invoice and vouchers when imported if possible. Default: 1.
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, CheckAccountUpdateModelType] = UNSET
    import_type: Union[Unset, None, CheckAccountUpdateModelImportType] = UNSET
    currency: Union[Unset, str] = UNSET
    default_account: Union[
        Unset, CheckAccountUpdateModelDefaultAccount
    ] = CheckAccountUpdateModelDefaultAccount.VALUE_0
    status: Union[
        Unset, CheckAccountUpdateModelStatus
    ] = CheckAccountUpdateModelStatus.VALUE_100
    auto_map_transactions: Union[Unset, None, int] = 1
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        import_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.import_type, Unset):
            import_type = self.import_type.value if self.import_type else None

        currency = self.currency
        default_account: Union[Unset, int] = UNSET
        if not isinstance(self.default_account, Unset):
            default_account = self.default_account.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        auto_map_transactions = self.auto_map_transactions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if import_type is not UNSET:
            field_dict["importType"] = import_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if default_account is not UNSET:
            field_dict["defaultAccount"] = default_account
        if status is not UNSET:
            field_dict["status"] = status
        if auto_map_transactions is not UNSET:
            field_dict["autoMapTransactions"] = auto_map_transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CheckAccountUpdateModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CheckAccountUpdateModelType(_type)

        _import_type = d.pop("importType", UNSET)
        import_type: Union[Unset, None, CheckAccountUpdateModelImportType]
        if _import_type is None:
            import_type = None
        elif isinstance(_import_type, Unset):
            import_type = UNSET
        else:
            import_type = CheckAccountUpdateModelImportType(_import_type)

        currency = d.pop("currency", UNSET)

        _default_account = d.pop("defaultAccount", UNSET)
        default_account: Union[Unset, CheckAccountUpdateModelDefaultAccount]
        if isinstance(_default_account, Unset):
            default_account = UNSET
        else:
            default_account = CheckAccountUpdateModelDefaultAccount(_default_account)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CheckAccountUpdateModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CheckAccountUpdateModelStatus(_status)

        auto_map_transactions = d.pop("autoMapTransactions", UNSET)

        check_account_update_model = cls(
            name=name,
            type=type,
            import_type=import_type,
            currency=currency,
            default_account=default_account,
            status=status,
            auto_map_transactions=auto_map_transactions,
        )

        check_account_update_model.additional_properties = d
        return check_account_update_model

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
