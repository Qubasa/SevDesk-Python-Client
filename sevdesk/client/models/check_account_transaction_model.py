import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.check_account_transaction_model_status import (
    CheckAccountTransactionModelStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_account_transaction_model_check_account import (
        CheckAccountTransactionModelCheckAccount,
    )
    from ..models.check_account_transaction_model_sev_client import (
        CheckAccountTransactionModelSevClient,
    )
    from ..models.check_account_transaction_model_source_transaction import (
        CheckAccountTransactionModelSourceTransaction,
    )
    from ..models.check_account_transaction_model_target_transaction import (
        CheckAccountTransactionModelTargetTransaction,
    )


T = TypeVar("T", bound="CheckAccountTransactionModel")


@attr.s(auto_attribs=True)
class CheckAccountTransactionModel:
    """CheckAccountTransaction model. Responsible for the transactions on payment accounts.

    Attributes:
        value_date (datetime.datetime): Date the check account transaction was booked Example: 01.01.2022.
        amount (float): Amount of the transaction Example: 100.
        payee_payer_name (str): Name of the payee/payer Example: Cercei Lannister.
        check_account (CheckAccountTransactionModelCheckAccount): The check account to which the transaction belongs
        status (CheckAccountTransactionModelStatus): Status of the check account transaction.<br>
                 100 <-> Created<br>
                 200 <-> Linked<br>
                 300 <-> Private<br>
                 400 <-> Booked
        id (Union[Unset, int]): The check account transaction id
        object_name (Union[Unset, str]): The check account transaction object name
        create (Union[Unset, datetime.datetime]): Date of check account transaction creation
        update (Union[Unset, datetime.datetime]): Date of last check account transaction update
        sev_client (Union[Unset, CheckAccountTransactionModelSevClient]): Client to which check account transaction
            belongs. Will be filled automatically
        entry_date (Union[Unset, datetime.datetime]): Date the check account transaction was imported Example:
            01.01.2022.
        paymt_purpose (Union[Unset, str]): the purpose of the transaction Example: salary.
        enshrined (Union[Unset, None, datetime.datetime]): Defines if the transaction has been enshrined and can not be
            changed any more.
        source_transaction (Union[Unset, None, CheckAccountTransactionModelSourceTransaction]): The check account
            transaction serving as the source of the rebooking
        target_transaction (Union[Unset, None, CheckAccountTransactionModelTargetTransaction]): The check account
            transaction serving as the target of the rebooking
    """

    value_date: datetime.datetime
    amount: float
    payee_payer_name: str
    check_account: "CheckAccountTransactionModelCheckAccount"
    status: CheckAccountTransactionModelStatus
    id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    sev_client: Union[Unset, "CheckAccountTransactionModelSevClient"] = UNSET
    entry_date: Union[Unset, datetime.datetime] = UNSET
    paymt_purpose: Union[Unset, str] = UNSET
    enshrined: Union[Unset, None, datetime.datetime] = UNSET
    source_transaction: Union[
        Unset, None, "CheckAccountTransactionModelSourceTransaction"
    ] = UNSET
    target_transaction: Union[
        Unset, None, "CheckAccountTransactionModelTargetTransaction"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value_date = self.value_date.isoformat()

        amount = self.amount
        payee_payer_name = self.payee_payer_name
        check_account = self.check_account.to_dict()

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

        entry_date: Union[Unset, str] = UNSET
        if not isinstance(self.entry_date, Unset):
            entry_date = self.entry_date.isoformat()

        paymt_purpose = self.paymt_purpose
        enshrined: Union[Unset, None, str] = UNSET
        if not isinstance(self.enshrined, Unset):
            enshrined = self.enshrined.isoformat() if self.enshrined else None

        source_transaction: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source_transaction, Unset):
            source_transaction = (
                self.source_transaction.to_dict() if self.source_transaction else None
            )

        target_transaction: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.target_transaction, Unset):
            target_transaction = (
                self.target_transaction.to_dict() if self.target_transaction else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valueDate": value_date,
                "amount": amount,
                "payeePayerName": payee_payer_name,
                "checkAccount": check_account,
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
        if entry_date is not UNSET:
            field_dict["entryDate"] = entry_date
        if paymt_purpose is not UNSET:
            field_dict["paymtPurpose"] = paymt_purpose
        if enshrined is not UNSET:
            field_dict["enshrined"] = enshrined
        if source_transaction is not UNSET:
            field_dict["sourceTransaction"] = source_transaction
        if target_transaction is not UNSET:
            field_dict["targetTransaction"] = target_transaction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_account_transaction_model_check_account import (
            CheckAccountTransactionModelCheckAccount,
        )
        from ..models.check_account_transaction_model_sev_client import (
            CheckAccountTransactionModelSevClient,
        )
        from ..models.check_account_transaction_model_source_transaction import (
            CheckAccountTransactionModelSourceTransaction,
        )
        from ..models.check_account_transaction_model_target_transaction import (
            CheckAccountTransactionModelTargetTransaction,
        )

        d = src_dict.copy()
        value_date = isoparse(d.pop("valueDate"))

        amount = d.pop("amount")

        payee_payer_name = d.pop("payeePayerName")

        check_account = CheckAccountTransactionModelCheckAccount.from_dict(
            d.pop("checkAccount")
        )

        status = CheckAccountTransactionModelStatus(d.pop("status"))

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
        sev_client: Union[Unset, CheckAccountTransactionModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = CheckAccountTransactionModelSevClient.from_dict(_sev_client)

        _entry_date = d.pop("entryDate", UNSET)
        entry_date: Union[Unset, datetime.datetime]
        if isinstance(_entry_date, Unset):
            entry_date = UNSET
        else:
            entry_date = isoparse(_entry_date)

        paymt_purpose = d.pop("paymtPurpose", UNSET)

        _enshrined = d.pop("enshrined", UNSET)
        enshrined: Union[Unset, None, datetime.datetime]
        if _enshrined is None:
            enshrined = None
        elif isinstance(_enshrined, Unset):
            enshrined = UNSET
        else:
            enshrined = isoparse(_enshrined)

        _source_transaction = d.pop("sourceTransaction", UNSET)
        source_transaction: Union[
            Unset, None, CheckAccountTransactionModelSourceTransaction
        ]
        if _source_transaction is None:
            source_transaction = None
        elif isinstance(_source_transaction, Unset):
            source_transaction = UNSET
        else:
            source_transaction = (
                CheckAccountTransactionModelSourceTransaction.from_dict(
                    _source_transaction
                )
            )

        _target_transaction = d.pop("targetTransaction", UNSET)
        target_transaction: Union[
            Unset, None, CheckAccountTransactionModelTargetTransaction
        ]
        if _target_transaction is None:
            target_transaction = None
        elif isinstance(_target_transaction, Unset):
            target_transaction = UNSET
        else:
            target_transaction = (
                CheckAccountTransactionModelTargetTransaction.from_dict(
                    _target_transaction
                )
            )

        check_account_transaction_model = cls(
            value_date=value_date,
            amount=amount,
            payee_payer_name=payee_payer_name,
            check_account=check_account,
            status=status,
            id=id,
            object_name=object_name,
            create=create,
            update=update,
            sev_client=sev_client,
            entry_date=entry_date,
            paymt_purpose=paymt_purpose,
            enshrined=enshrined,
            source_transaction=source_transaction,
            target_transaction=target_transaction,
        )

        check_account_transaction_model.additional_properties = d
        return check_account_transaction_model

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
