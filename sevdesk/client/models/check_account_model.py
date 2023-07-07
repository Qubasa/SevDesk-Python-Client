import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.check_account_model_default_account import CheckAccountModelDefaultAccount
from ..models.check_account_model_import_type import CheckAccountModelImportType
from ..models.check_account_model_status import CheckAccountModelStatus
from ..models.check_account_model_type import CheckAccountModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_account_model_sev_client import CheckAccountModelSevClient


T = TypeVar("T", bound="CheckAccountModel")


@attr.s(auto_attribs=True)
class CheckAccountModel:
    """CheckAccount model. Responsible for the payment accounts.

    Attributes:
        name (str): Name of the check account Example: Iron Bank.
        type (CheckAccountModelType): The type of the check account. Account with a CSV or MT940 import are regarded as
            online.<br>
                 Apart from that, created check accounts over the API need to be offline, as online accounts with an active
            connection
                 to a bank application can not be managed over the API. Example: online.
        currency (str): The currency of the check account. Example: EUR.
        status (CheckAccountModelStatus): Status of the check account. 0 <-> Archived - 100 <-> Active Default:
            CheckAccountModelStatus.VALUE_100.
        id (Union[Unset, int]): The check account id
        object_name (Union[Unset, str]): The check account object name
        create (Union[Unset, datetime.datetime]): Date of check account creation
        update (Union[Unset, datetime.datetime]): Date of last check account update
        sev_client (Union[Unset, CheckAccountModelSevClient]): Client to which check account belongs. Will be filled
            automatically
        import_type (Union[Unset, None, CheckAccountModelImportType]): Import type. Transactions can be imported by this
            method on the check account. Example: CSV.
        default_account (Union[Unset, CheckAccountModelDefaultAccount]): Defines if this check account is the default
            account. Default: CheckAccountModelDefaultAccount.VALUE_0.
        bank_server (Union[Unset, str]): Bank server of check account
        auto_map_transactions (Union[Unset, None, int]): Defines if transactions on this account are automatically
            mapped to invoice and vouchers when imported if possible. Default: 1.
    """

    name: str
    type: CheckAccountModelType
    currency: str
    status: CheckAccountModelStatus = CheckAccountModelStatus.VALUE_100
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    sev_client: Union[Unset, "CheckAccountModelSevClient"] = UNSET
    import_type: Union[Unset, None, CheckAccountModelImportType] = UNSET
    default_account: Union[
        Unset, CheckAccountModelDefaultAccount
    ] = CheckAccountModelDefaultAccount.VALUE_0
    bank_server: Union[Unset, str] = UNSET
    auto_map_transactions: Union[Unset, None, int] = 1
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        currency = self.currency
        status = self.status.value

        id = self.id
        object_name = self.object_name
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        import_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.import_type, Unset):
            import_type = self.import_type.value if self.import_type else None

        default_account: Union[Unset, int] = UNSET
        if not isinstance(self.default_account, Unset):
            default_account = self.default_account.value

        bank_server = self.bank_server
        auto_map_transactions = self.auto_map_transactions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "currency": currency,
                "status": status,
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
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if import_type is not UNSET:
            field_dict["importType"] = import_type
        if default_account is not UNSET:
            field_dict["defaultAccount"] = default_account
        if bank_server is not UNSET:
            field_dict["bankServer"] = bank_server
        if auto_map_transactions is not UNSET:
            field_dict["autoMapTransactions"] = auto_map_transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_account_model_sev_client import CheckAccountModelSevClient

        d = src_dict.copy()
        name = d.pop("name")

        type = CheckAccountModelType(d.pop("type"))

        currency = d.pop("currency")

        status = CheckAccountModelStatus(d.pop("status"))

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

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, CheckAccountModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = CheckAccountModelSevClient.from_dict(_sev_client)

        _import_type = d.pop("importType", UNSET)
        import_type: Union[Unset, None, CheckAccountModelImportType]
        if _import_type is None:
            import_type = None
        elif isinstance(_import_type, Unset):
            import_type = UNSET
        else:
            import_type = CheckAccountModelImportType(_import_type)

        _default_account = d.pop("defaultAccount", UNSET)
        default_account: Union[Unset, CheckAccountModelDefaultAccount]
        if isinstance(_default_account, Unset):
            default_account = UNSET
        else:
            default_account = CheckAccountModelDefaultAccount(_default_account)

        bank_server = d.pop("bankServer", UNSET)

        auto_map_transactions = d.pop("autoMapTransactions", UNSET)

        check_account_model = cls(
            name=name,
            type=type,
            currency=currency,
            status=status,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            sev_client=sev_client,
            import_type=import_type,
            default_account=default_account,
            bank_server=bank_server,
            auto_map_transactions=auto_map_transactions,
        )

        check_account_model.additional_properties = d
        return check_account_model

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
