import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.voucher_response_model_credit_debit import VoucherResponseModelCreditDebit
from ..models.voucher_response_model_recurring_interval import (
    VoucherResponseModelRecurringInterval,
)
from ..models.voucher_response_model_status import VoucherResponseModelStatus
from ..models.voucher_response_model_voucher_type import VoucherResponseModelVoucherType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voucher_response_model_cost_centre import (
        VoucherResponseModelCostCentre,
    )
    from ..models.voucher_response_model_create_user import (
        VoucherResponseModelCreateUser,
    )
    from ..models.voucher_response_model_document import VoucherResponseModelDocument
    from ..models.voucher_response_model_sev_client import VoucherResponseModelSevClient
    from ..models.voucher_response_model_supplier import VoucherResponseModelSupplier
    from ..models.voucher_response_model_tax_set import VoucherResponseModelTaxSet


T = TypeVar("T", bound="VoucherResponseModel")


@attr.s(auto_attribs=True)
class VoucherResponseModel:
    """Voucher model

    Attributes:
        object_name (str): The voucher object name
        map_all (bool):  Example: True.
        status (VoucherResponseModelStatus): Please have a look in
                <a href='https://api.sevdesk.de/#section/Types-and-status-of-vouchers'>status of vouchers</a>
                to see what the different status codes mean Example: 50.
        tax_type (str): Tax type of the voucher.
            There are four tax types:
            1. default - Umsatzsteuer ausweisen
            2. eu - Steuerfreie innergemeinschaftliche Lieferung (Europäische Union)
            3. noteu - Steuerschuldnerschaft des Leistungsempfängers (außerhalb EU, z. B. Schweiz)
            4. custom - Using custom tax set
            5. ss - Not subject to VAT according to §19 1 UStG
            Tax rates are heavily connected to the tax type used. Example: default.
        credit_debit (VoucherResponseModelCreditDebit): Defines if your voucher is a credit (C) or debit (D) Example: C.
        voucher_type (VoucherResponseModelVoucherType): Type of the voucher. For more information on the different
            types, check
                 <a href='https://api.sevdesk.de/#section/Types-and-status-of-vouchers'>this</a>
             Example: VOU.
        id (Union[Unset, int]): The voucher id
        create (Union[Unset, datetime.datetime]): Date of voucher creation Example: 01.01.2020.
        update (Union[Unset, datetime.datetime]): Date of last voucher update Example: 01.01.2020.
        sev_client (Union[Unset, VoucherResponseModelSevClient]): Client to which voucher belongs. Will be filled
            automatically
        create_user (Union[Unset, VoucherResponseModelCreateUser]): User who created the voucher. Will be filled
            automatically.
        voucher_date (Union[Unset, None, datetime.datetime]): Needs to be provided as timestamp or dd.mm.yyyy Example:
            01.01.2022.
        supplier (Union[Unset, None, VoucherResponseModelSupplier]): The contact used in the voucher as a supplier.<br>
            If you don't have a contact as a supplier, you can set this object to null.
        supplier_name (Union[Unset, None, str]): The supplier name.<br>
                 The value you provide here will determine what supplier name is shown for the voucher in case you did not
            provide a supplier. Example: John Snow.
        description (Union[Unset, None, str]): The description of the voucher. Essentially the voucher number. Example:
            Voucher-1000.
        pay_date (Union[Unset, None, datetime.datetime]): Needs to be timestamp or dd.mm.yyyy Example: 01.01.2022.
        sum_net (Union[Unset, float]): Net sum of the voucher
        sum_tax (Union[Unset, float]): Tax sum of the voucher
        sum_gross (Union[Unset, float]): Gross sum of the voucher
        sum_net_accounting (Union[Unset, float]): Net accounting sum of the voucher. Is usually the same as sumNet
        sum_tax_accounting (Union[Unset, float]): Tax accounting sum of the voucher. Is usually the same as sumTax
        sum_gross_accounting (Union[Unset, float]): Gross accounting sum of the voucher. Is usually the same as sumGross
        sum_discounts (Union[Unset, float]): Sum of all discounts in the voucher
        sum_discounts_foreign_currency (Union[Unset, float]): Discounts sum of the voucher in the foreign currency
        paid_amount (Union[Unset, None, float]): Amount which has already been paid for this voucher by the customer
        currency (Union[Unset, None, str]): specifies which currency the voucher should have. Attention: If the currency
            differs from the default currency stored in the account, then either the "propertyForeignCurrencyDeadline" or
            "propertyExchangeRate" parameter must be specified. If both parameters are specified, then the
            "propertyForeignCurrencyDeadline" parameter is preferred Example: EUR.
        property_foreign_currency_deadline (Union[Unset, None, datetime.datetime]): Defines the exchange rate day and
            and then the exchange rate is set from sevDesk. Needs to be provided as timestamp or dd.mm.yyyy Example:
            01.01.2022.
        property_exchange_rate (Union[Unset, None, float]): Defines the exchange rate Example: 0.8912.
        recurring_interval (Union[Unset, None, VoucherResponseModelRecurringInterval]): The DateInterval in which
            recurring vouchers are generated.<br>
                 Necessary attribute for all recurring vouchers.
        recurring_start_date (Union[Unset, None, datetime.datetime]): The date when the recurring vouchers start being
            generated.<br>
                 Necessary attribute for all recurring vouchers. Example: 01.01.2020.
        recurring_next_voucher (Union[Unset, None, datetime.datetime]): The date when the next voucher should be
            generated.<br>
                 Necessary attribute for all recurring vouchers. Example: 01.02.2020.
        recurring_last_voucher (Union[Unset, None, datetime.datetime]): The date when the last voucher was generated.
            Example: 01.01.2021.
        recurring_end_date (Union[Unset, None, datetime.datetime]): The date when the recurring vouchers end being
            generated.<br>
                Necessary attribute for all recurring vouchers. Example: 01.01.2021.
        enshrined (Union[Unset, None, datetime.datetime]): Defines if and when voucher was enshrined. Enshrined vouchers
            can not be manipulated. Example: 01.01.2020.
        tax_set (Union[Unset, None, VoucherResponseModelTaxSet]): Tax set of the voucher. Needs to be added if you chose
            the tax type custom
        payment_deadline (Union[Unset, None, datetime.datetime]): Payment deadline of the voucher. Example: 01.01.2022.
        delivery_date (Union[Unset, datetime.datetime]): Needs to be provided as timestamp or dd.mm.yyyy Example:
            01.01.2022.
        delivery_date_until (Union[Unset, None, datetime.datetime]): Needs to be provided as timestamp or dd.mm.yyyy
            Example: 22.02.2022.
        document (Union[Unset, None, VoucherResponseModelDocument]): The document of the voucher.
        cost_centre (Union[Unset, VoucherResponseModelCostCentre]): Cost centre for the voucher
    """

    object_name: str
    map_all: bool
    status: VoucherResponseModelStatus
    tax_type: str
    credit_debit: VoucherResponseModelCreditDebit
    voucher_type: VoucherResponseModelVoucherType
    id: Union[Unset, int] = UNSET
    create: Union[Unset, datetime.datetime] = UNSET
    update: Union[Unset, datetime.datetime] = UNSET
    sev_client: Union[Unset, "VoucherResponseModelSevClient"] = UNSET
    create_user: Union[Unset, "VoucherResponseModelCreateUser"] = UNSET
    voucher_date: Union[Unset, None, datetime.datetime] = UNSET
    supplier: Union[Unset, None, "VoucherResponseModelSupplier"] = UNSET
    supplier_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    pay_date: Union[Unset, None, datetime.datetime] = UNSET
    sum_net: Union[Unset, float] = UNSET
    sum_tax: Union[Unset, float] = UNSET
    sum_gross: Union[Unset, float] = UNSET
    sum_net_accounting: Union[Unset, float] = UNSET
    sum_tax_accounting: Union[Unset, float] = UNSET
    sum_gross_accounting: Union[Unset, float] = UNSET
    sum_discounts: Union[Unset, float] = UNSET
    sum_discounts_foreign_currency: Union[Unset, float] = UNSET
    paid_amount: Union[Unset, None, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    property_foreign_currency_deadline: Union[Unset, None, datetime.datetime] = UNSET
    property_exchange_rate: Union[Unset, None, float] = UNSET
    recurring_interval: Union[
        Unset, None, VoucherResponseModelRecurringInterval
    ] = UNSET
    recurring_start_date: Union[Unset, None, datetime.datetime] = UNSET
    recurring_next_voucher: Union[Unset, None, datetime.datetime] = UNSET
    recurring_last_voucher: Union[Unset, None, datetime.datetime] = UNSET
    recurring_end_date: Union[Unset, None, datetime.datetime] = UNSET
    enshrined: Union[Unset, None, datetime.datetime] = UNSET
    tax_set: Union[Unset, None, "VoucherResponseModelTaxSet"] = UNSET
    payment_deadline: Union[Unset, None, datetime.datetime] = UNSET
    delivery_date: Union[Unset, datetime.datetime] = UNSET
    delivery_date_until: Union[Unset, None, datetime.datetime] = UNSET
    document: Union[Unset, None, "VoucherResponseModelDocument"] = UNSET
    cost_centre: Union[Unset, "VoucherResponseModelCostCentre"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_name = self.object_name
        map_all = self.map_all
        status = self.status.value

        tax_type = self.tax_type
        credit_debit = self.credit_debit.value

        voucher_type = self.voucher_type.value

        id = self.id
        create: Union[Unset, str] = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.isoformat()

        update: Union[Unset, str] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.isoformat()

        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        create_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_user, Unset):
            create_user = self.create_user.to_dict()

        voucher_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.voucher_date, Unset):
            voucher_date = self.voucher_date.isoformat() if self.voucher_date else None

        supplier: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict() if self.supplier else None

        supplier_name = self.supplier_name
        description = self.description
        pay_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.pay_date, Unset):
            pay_date = self.pay_date.isoformat() if self.pay_date else None

        sum_net = self.sum_net
        sum_tax = self.sum_tax
        sum_gross = self.sum_gross
        sum_net_accounting = self.sum_net_accounting
        sum_tax_accounting = self.sum_tax_accounting
        sum_gross_accounting = self.sum_gross_accounting
        sum_discounts = self.sum_discounts
        sum_discounts_foreign_currency = self.sum_discounts_foreign_currency
        paid_amount = self.paid_amount
        currency = self.currency
        property_foreign_currency_deadline: Union[Unset, None, str] = UNSET
        if not isinstance(self.property_foreign_currency_deadline, Unset):
            property_foreign_currency_deadline = (
                self.property_foreign_currency_deadline.isoformat()
                if self.property_foreign_currency_deadline
                else None
            )

        property_exchange_rate = self.property_exchange_rate
        recurring_interval: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurring_interval, Unset):
            recurring_interval = (
                self.recurring_interval.value if self.recurring_interval else None
            )

        recurring_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurring_start_date, Unset):
            recurring_start_date = (
                self.recurring_start_date.isoformat()
                if self.recurring_start_date
                else None
            )

        recurring_next_voucher: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurring_next_voucher, Unset):
            recurring_next_voucher = (
                self.recurring_next_voucher.isoformat()
                if self.recurring_next_voucher
                else None
            )

        recurring_last_voucher: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurring_last_voucher, Unset):
            recurring_last_voucher = (
                self.recurring_last_voucher.isoformat()
                if self.recurring_last_voucher
                else None
            )

        recurring_end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurring_end_date, Unset):
            recurring_end_date = (
                self.recurring_end_date.isoformat() if self.recurring_end_date else None
            )

        enshrined: Union[Unset, None, str] = UNSET
        if not isinstance(self.enshrined, Unset):
            enshrined = self.enshrined.isoformat() if self.enshrined else None

        tax_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_set, Unset):
            tax_set = self.tax_set.to_dict() if self.tax_set else None

        payment_deadline: Union[Unset, None, str] = UNSET
        if not isinstance(self.payment_deadline, Unset):
            payment_deadline = (
                self.payment_deadline.isoformat() if self.payment_deadline else None
            )

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        delivery_date_until: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivery_date_until, Unset):
            delivery_date_until = (
                self.delivery_date_until.isoformat()
                if self.delivery_date_until
                else None
            )

        document: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict() if self.document else None

        cost_centre: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_centre, Unset):
            cost_centre = self.cost_centre.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objectName": object_name,
                "mapAll": map_all,
                "status": status,
                "taxType": tax_type,
                "creditDebit": credit_debit,
                "voucherType": voucher_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if sev_client is not UNSET:
            field_dict["sevClient"] = sev_client
        if create_user is not UNSET:
            field_dict["createUser"] = create_user
        if voucher_date is not UNSET:
            field_dict["voucherDate"] = voucher_date
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if description is not UNSET:
            field_dict["description"] = description
        if pay_date is not UNSET:
            field_dict["payDate"] = pay_date
        if sum_net is not UNSET:
            field_dict["sumNet"] = sum_net
        if sum_tax is not UNSET:
            field_dict["sumTax"] = sum_tax
        if sum_gross is not UNSET:
            field_dict["sumGross"] = sum_gross
        if sum_net_accounting is not UNSET:
            field_dict["sumNetAccounting"] = sum_net_accounting
        if sum_tax_accounting is not UNSET:
            field_dict["sumTaxAccounting"] = sum_tax_accounting
        if sum_gross_accounting is not UNSET:
            field_dict["sumGrossAccounting"] = sum_gross_accounting
        if sum_discounts is not UNSET:
            field_dict["sumDiscounts"] = sum_discounts
        if sum_discounts_foreign_currency is not UNSET:
            field_dict["sumDiscountsForeignCurrency"] = sum_discounts_foreign_currency
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if property_foreign_currency_deadline is not UNSET:
            field_dict[
                "propertyForeignCurrencyDeadline"
            ] = property_foreign_currency_deadline
        if property_exchange_rate is not UNSET:
            field_dict["propertyExchangeRate"] = property_exchange_rate
        if recurring_interval is not UNSET:
            field_dict["recurringInterval"] = recurring_interval
        if recurring_start_date is not UNSET:
            field_dict["recurringStartDate"] = recurring_start_date
        if recurring_next_voucher is not UNSET:
            field_dict["recurringNextVoucher"] = recurring_next_voucher
        if recurring_last_voucher is not UNSET:
            field_dict["recurringLastVoucher"] = recurring_last_voucher
        if recurring_end_date is not UNSET:
            field_dict["recurringEndDate"] = recurring_end_date
        if enshrined is not UNSET:
            field_dict["enshrined"] = enshrined
        if tax_set is not UNSET:
            field_dict["taxSet"] = tax_set
        if payment_deadline is not UNSET:
            field_dict["paymentDeadline"] = payment_deadline
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if delivery_date_until is not UNSET:
            field_dict["deliveryDateUntil"] = delivery_date_until
        if document is not UNSET:
            field_dict["document"] = document
        if cost_centre is not UNSET:
            field_dict["costCentre"] = cost_centre

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.voucher_response_model_cost_centre import (
            VoucherResponseModelCostCentre,
        )
        from ..models.voucher_response_model_create_user import (
            VoucherResponseModelCreateUser,
        )
        from ..models.voucher_response_model_document import (
            VoucherResponseModelDocument,
        )
        from ..models.voucher_response_model_sev_client import (
            VoucherResponseModelSevClient,
        )
        from ..models.voucher_response_model_supplier import (
            VoucherResponseModelSupplier,
        )
        from ..models.voucher_response_model_tax_set import VoucherResponseModelTaxSet

        d = src_dict.copy()
        object_name = d.pop("objectName")

        map_all = d.pop("mapAll")

        status = VoucherResponseModelStatus(d.pop("status"))

        tax_type = d.pop("taxType")

        credit_debit = VoucherResponseModelCreditDebit(d.pop("creditDebit"))

        voucher_type = VoucherResponseModelVoucherType(d.pop("voucherType"))

        id = d.pop("id", UNSET)

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
        sev_client: Union[Unset, VoucherResponseModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = VoucherResponseModelSevClient.from_dict(_sev_client)

        _create_user = d.pop("createUser", UNSET)
        create_user: Union[Unset, VoucherResponseModelCreateUser]
        if isinstance(_create_user, Unset):
            create_user = UNSET
        else:
            create_user = VoucherResponseModelCreateUser.from_dict(_create_user)

        _voucher_date = d.pop("voucherDate", UNSET)
        voucher_date: Union[Unset, None, datetime.datetime]
        if _voucher_date is None:
            voucher_date = None
        elif isinstance(_voucher_date, Unset):
            voucher_date = UNSET
        else:
            voucher_date = isoparse(_voucher_date)

        _supplier = d.pop("supplier", UNSET)
        supplier: Union[Unset, None, VoucherResponseModelSupplier]
        if _supplier is None:
            supplier = None
        elif isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = VoucherResponseModelSupplier.from_dict(_supplier)

        supplier_name = d.pop("supplierName", UNSET)

        description = d.pop("description", UNSET)

        _pay_date = d.pop("payDate", UNSET)
        pay_date: Union[Unset, None, datetime.datetime]
        if _pay_date is None:
            pay_date = None
        elif isinstance(_pay_date, Unset):
            pay_date = UNSET
        else:
            pay_date = isoparse(_pay_date)

        sum_net = d.pop("sumNet", UNSET)

        sum_tax = d.pop("sumTax", UNSET)

        sum_gross = d.pop("sumGross", UNSET)

        sum_net_accounting = d.pop("sumNetAccounting", UNSET)

        sum_tax_accounting = d.pop("sumTaxAccounting", UNSET)

        sum_gross_accounting = d.pop("sumGrossAccounting", UNSET)

        sum_discounts = d.pop("sumDiscounts", UNSET)

        sum_discounts_foreign_currency = d.pop("sumDiscountsForeignCurrency", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        currency = d.pop("currency", UNSET)

        _property_foreign_currency_deadline = d.pop(
            "propertyForeignCurrencyDeadline", UNSET
        )
        property_foreign_currency_deadline: Union[Unset, None, datetime.datetime]
        if _property_foreign_currency_deadline is None:
            property_foreign_currency_deadline = None
        elif isinstance(_property_foreign_currency_deadline, Unset):
            property_foreign_currency_deadline = UNSET
        else:
            property_foreign_currency_deadline = isoparse(
                _property_foreign_currency_deadline
            )

        property_exchange_rate = d.pop("propertyExchangeRate", UNSET)

        _recurring_interval = d.pop("recurringInterval", UNSET)
        recurring_interval: Union[Unset, None, VoucherResponseModelRecurringInterval]
        if _recurring_interval is None:
            recurring_interval = None
        elif isinstance(_recurring_interval, Unset):
            recurring_interval = UNSET
        else:
            recurring_interval = VoucherResponseModelRecurringInterval(
                _recurring_interval
            )

        _recurring_start_date = d.pop("recurringStartDate", UNSET)
        recurring_start_date: Union[Unset, None, datetime.datetime]
        if _recurring_start_date is None:
            recurring_start_date = None
        elif isinstance(_recurring_start_date, Unset):
            recurring_start_date = UNSET
        else:
            recurring_start_date = isoparse(_recurring_start_date)

        _recurring_next_voucher = d.pop("recurringNextVoucher", UNSET)
        recurring_next_voucher: Union[Unset, None, datetime.datetime]
        if _recurring_next_voucher is None:
            recurring_next_voucher = None
        elif isinstance(_recurring_next_voucher, Unset):
            recurring_next_voucher = UNSET
        else:
            recurring_next_voucher = isoparse(_recurring_next_voucher)

        _recurring_last_voucher = d.pop("recurringLastVoucher", UNSET)
        recurring_last_voucher: Union[Unset, None, datetime.datetime]
        if _recurring_last_voucher is None:
            recurring_last_voucher = None
        elif isinstance(_recurring_last_voucher, Unset):
            recurring_last_voucher = UNSET
        else:
            recurring_last_voucher = isoparse(_recurring_last_voucher)

        _recurring_end_date = d.pop("recurringEndDate", UNSET)
        recurring_end_date: Union[Unset, None, datetime.datetime]
        if _recurring_end_date is None:
            recurring_end_date = None
        elif isinstance(_recurring_end_date, Unset):
            recurring_end_date = UNSET
        else:
            recurring_end_date = isoparse(_recurring_end_date)

        _enshrined = d.pop("enshrined", UNSET)
        enshrined: Union[Unset, None, datetime.datetime]
        if _enshrined is None:
            enshrined = None
        elif isinstance(_enshrined, Unset):
            enshrined = UNSET
        else:
            enshrined = isoparse(_enshrined)

        _tax_set = d.pop("taxSet", UNSET)
        tax_set: Union[Unset, None, VoucherResponseModelTaxSet]
        if _tax_set is None:
            tax_set = None
        elif isinstance(_tax_set, Unset):
            tax_set = UNSET
        else:
            tax_set = VoucherResponseModelTaxSet.from_dict(_tax_set)

        _payment_deadline = d.pop("paymentDeadline", UNSET)
        payment_deadline: Union[Unset, None, datetime.datetime]
        if _payment_deadline is None:
            payment_deadline = None
        elif isinstance(_payment_deadline, Unset):
            payment_deadline = UNSET
        else:
            payment_deadline = isoparse(_payment_deadline)

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date)

        _delivery_date_until = d.pop("deliveryDateUntil", UNSET)
        delivery_date_until: Union[Unset, None, datetime.datetime]
        if _delivery_date_until is None:
            delivery_date_until = None
        elif isinstance(_delivery_date_until, Unset):
            delivery_date_until = UNSET
        else:
            delivery_date_until = isoparse(_delivery_date_until)

        _document = d.pop("document", UNSET)
        document: Union[Unset, None, VoucherResponseModelDocument]
        if _document is None:
            document = None
        elif isinstance(_document, Unset):
            document = UNSET
        else:
            document = VoucherResponseModelDocument.from_dict(_document)

        _cost_centre = d.pop("costCentre", UNSET)
        cost_centre: Union[Unset, VoucherResponseModelCostCentre]
        if isinstance(_cost_centre, Unset):
            cost_centre = UNSET
        else:
            cost_centre = VoucherResponseModelCostCentre.from_dict(_cost_centre)

        voucher_response_model = cls(
            object_name=object_name,
            map_all=map_all,
            status=status,
            tax_type=tax_type,
            credit_debit=credit_debit,
            voucher_type=voucher_type,
            id=id,
            create=create,
            update=update,
            sev_client=sev_client,
            create_user=create_user,
            voucher_date=voucher_date,
            supplier=supplier,
            supplier_name=supplier_name,
            description=description,
            pay_date=pay_date,
            sum_net=sum_net,
            sum_tax=sum_tax,
            sum_gross=sum_gross,
            sum_net_accounting=sum_net_accounting,
            sum_tax_accounting=sum_tax_accounting,
            sum_gross_accounting=sum_gross_accounting,
            sum_discounts=sum_discounts,
            sum_discounts_foreign_currency=sum_discounts_foreign_currency,
            paid_amount=paid_amount,
            currency=currency,
            property_foreign_currency_deadline=property_foreign_currency_deadline,
            property_exchange_rate=property_exchange_rate,
            recurring_interval=recurring_interval,
            recurring_start_date=recurring_start_date,
            recurring_next_voucher=recurring_next_voucher,
            recurring_last_voucher=recurring_last_voucher,
            recurring_end_date=recurring_end_date,
            enshrined=enshrined,
            tax_set=tax_set,
            payment_deadline=payment_deadline,
            delivery_date=delivery_date,
            delivery_date_until=delivery_date_until,
            document=document,
            cost_centre=cost_centre,
        )

        voucher_response_model.additional_properties = d
        return voucher_response_model

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
