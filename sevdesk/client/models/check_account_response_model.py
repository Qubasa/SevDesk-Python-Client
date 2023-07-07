import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.check_account_response_model_import_type import (
    CheckAccountResponseModelImportType,
)
from ..models.check_account_response_model_status import CheckAccountResponseModelStatus
from ..models.check_account_response_model_type import CheckAccountResponseModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_account_response_model_sev_client import (
        CheckAccountResponseModelSevClient,
    )


T = TypeVar("T", bound="CheckAccountResponseModel")


@attr.s(auto_attribs=True)
class CheckAccountResponseModel:
    """CheckAccount model. Responsible for the payment accounts.

    Attributes:
        id (Union[Unset, str]): The check account id Example: 0.
        object_name (Union[Unset, str]): The check account object name Example: CheckAccount.
        create (Union[Unset, datetime.datetime]): Date of check account creation
        update (Union[Unset, datetime.datetime]): Date of last check account update
        sev_client (Union[Unset, CheckAccountResponseModelSevClient]): Client to which check account belongs. Will be
            filled automatically
        name (Union[Unset, str]): Name of the check account Example: Iron Bank.
        type (Union[Unset, CheckAccountResponseModelType]): The type of the check account. Account with a CSV or MT940
            import are regarded as online.<br>
                 Apart from that, created check accounts over the API need to be offline, as online accounts with an active
            connection
                 to a bank application can not be managed over the API. Example: online.
        import_type (Union[Unset, None, CheckAccountResponseModelImportType]): Import type. Transactions can be imported
            by this method on the check account. Example: CSV.
        currency (Union[Unset, str]): The currency of the check account. Example: EUR.
        default_account (Union[Unset, str]): Defines if this check account is the default account. Default: '0'.
        status (Union[Unset, CheckAccountResponseModelStatus]): Status of the check account. 0 <-> Archived - 100 <->
            Active Default: CheckAccountResponseModelStatus.VALUE_1.
        bank_server (Union[Unset, str]): Bank server of check account
        auto_map_transactions (Union[Unset, None, str]): Defines if transactions on this account are automatically
            mapped to invoice and vouchers when imported if possible. Default: '1'.
    """

    id: Union[Unset, str] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    sev_client: Union[Unset, "CheckAccountResponseModelSevClient"] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, CheckAccountResponseModelType] = UNSET
    import_type: Union[Unset, None, CheckAccountResponseModelImportType] = UNSET
    currency: Union[Unset, str] = UNSET
    default_account: Union[Unset, str] = "0"
    status: Union[
        Unset, CheckAccountResponseModelStatus
    ] = CheckAccountResponseModelStatus.VALUE_1
    bank_server: Union[Unset, str] = UNSET
    auto_map_transactions: Union[Unset, None, str] = "1"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        import_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.import_type, Unset):
            import_type = self.import_type.value if self.import_type else None

        currency = self.currency
        default_account = self.default_account
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        bank_server = self.bank_server
        auto_map_transactions = self.auto_map_transactions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if bank_server is not UNSET:
            field_dict["bankServer"] = bank_server
        if auto_map_transactions is not UNSET:
            field_dict["autoMapTransactions"] = auto_map_transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_account_response_model_sev_client import (
            CheckAccountResponseModelSevClient,
        )

        d = src_dict.copy()
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
        sev_client: Union[Unset, CheckAccountResponseModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = CheckAccountResponseModelSevClient.from_dict(_sev_client)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CheckAccountResponseModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CheckAccountResponseModelType(_type)

        _import_type = d.pop("importType", UNSET)
        import_type: Union[Unset, None, CheckAccountResponseModelImportType]
        if _import_type is None:
            import_type = None
        elif isinstance(_import_type, Unset):
            import_type = UNSET
        else:
            import_type = CheckAccountResponseModelImportType(_import_type)

        currency = d.pop("currency", UNSET)

        default_account = d.pop("defaultAccount", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CheckAccountResponseModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CheckAccountResponseModelStatus(_status)

        bank_server = d.pop("bankServer", UNSET)

        auto_map_transactions = d.pop("autoMapTransactions", UNSET)

        check_account_response_model = cls(
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            sev_client=sev_client,
            name=name,
            type=type,
            import_type=import_type,
            currency=currency,
            default_account=default_account,
            status=status,
            bank_server=bank_server,
            auto_map_transactions=auto_map_transactions,
        )

        check_account_response_model.additional_properties = d
        return check_account_response_model

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
