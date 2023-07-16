from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voucher_pos_model_accounting_type import VoucherPosModelAccountingType
    from ..models.voucher_pos_model_estimated_accounting_type import (
        VoucherPosModelEstimatedAccountingType,
    )
    from ..models.voucher_pos_model_sev_client import VoucherPosModelSevClient
    from ..models.voucher_pos_model_voucher import VoucherPosModelVoucher


T = TypeVar("T", bound="VoucherPosModel")


@attr.s(auto_attribs=True)
class VoucherPosModel:
    """Voucher position model

    Attributes:
        object_name (str): The voucher position object name
        map_all (bool):
        accounting_type (VoucherPosModelAccountingType): The accounting type to which the position belongs.<br>
                 An accounting type is the booking account to which the position belongs.<br>
                 For more information, please refer to
                 <a href='https://api.sevdesk.de/#section/Accounting-type'>this</a> section.
        tax_rate (float): Tax rate of the voucher position. Example: 19.
        net (bool): Determines whether 'sumNet' or 'sumGross' is regarded.<br>
                 If both are not given, 'sum' is regarded and treated as net or gross depending on 'net'.
             All positions must be either net or gross, a mixture of the two is not possible. Example: true.
        sum_net (float): Net sum of the voucher position.<br>
                Only regarded if 'net' is 'true', otherwise its readOnly. Example: 100.
        sum_gross (float): Gross sum of the voucher position.<br>
                Only regarded if 'net' is 'false', otherwise its readOnly. Example: 119.
        id (Union[Unset, int]): The voucher position id
        create (Union[Unset, str]): Date of voucher position creation Example: 01.01.2020.
        update (Union[Unset, str]): Date of last voucher position update Example: 01.01.2020.
        sev_client (Union[Unset, VoucherPosModelSevClient]): Client to which voucher position belongs. Will be filled
            automatically
        voucher (Optional[VoucherPosModelVoucher]): The voucher to which the position belongs.
        estimated_accounting_type (Union[Unset, VoucherPosModelEstimatedAccountingType]): The accounting type to which
            the position belongs estimated by our voucher recognition.<br>
                An accounting type is the booking account to which the position belongs.<br>
                For more information, please refer to
                <a href='https://api.sevdesk.de/#section/Accounting-type'>this</a> section.
        is_asset (Union[Unset, bool]): Determines whether position is regarded as an asset which can be depreciated.
            Example: false.
        sum_tax (Union[Unset, float]): Tax sum of the voucher position. Example: 19.
        sum_net_accounting (Union[Unset, float]): Net accounting sum. Is equal to sumNet.
        sum_tax_accounting (Union[Unset, float]): Tax accounting sum. Is equal to sumTax.
        sum_gross_accounting (Union[Unset, float]): Gross accounting sum. Is equal to sumGross.
        comment (Union[Unset, None, str]): Comment for the voucher position.
    """

    object_name: str
    map_all: bool
    accounting_type: "VoucherPosModelAccountingType"
    tax_rate: float
    net: bool
    sum_net: float
    sum_gross: float
    voucher: Optional["VoucherPosModelVoucher"]
    id: Union[Unset, int] = UNSET
    create: Union[Unset, str] = UNSET
    update: Union[Unset, str] = UNSET
    sev_client: Union[Unset, "VoucherPosModelSevClient"] = UNSET
    estimated_accounting_type: Union[
        Unset, "VoucherPosModelEstimatedAccountingType"
    ] = UNSET
    is_asset: Union[Unset, bool] = UNSET
    sum_tax: Union[Unset, float] = UNSET
    sum_net_accounting: Union[Unset, float] = UNSET
    sum_tax_accounting: Union[Unset, float] = UNSET
    sum_gross_accounting: Union[Unset, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_name = self.object_name
        map_all = self.map_all
        accounting_type = self.accounting_type.to_dict()

        tax_rate = self.tax_rate
        net = self.net
        sum_net = self.sum_net
        sum_gross = self.sum_gross
        id = self.id
        create = self.create
        update = self.update
        sev_client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sev_client, Unset):
            sev_client = self.sev_client.to_dict()

        voucher = self.voucher.to_dict() if self.voucher else None

        estimated_accounting_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_accounting_type, Unset):
            estimated_accounting_type = self.estimated_accounting_type.to_dict()

        is_asset = self.is_asset
        sum_tax = self.sum_tax
        sum_net_accounting = self.sum_net_accounting
        sum_tax_accounting = self.sum_tax_accounting
        sum_gross_accounting = self.sum_gross_accounting
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objectName": object_name,
                "mapAll": map_all,
                "accountingType": accounting_type,
                "taxRate": tax_rate,
                "net": net,
                "sumNet": sum_net,
                "sumGross": sum_gross,
                "voucher": voucher,
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
        if estimated_accounting_type is not UNSET:
            field_dict["estimatedAccountingType"] = estimated_accounting_type
        if is_asset is not UNSET:
            field_dict["isAsset"] = is_asset
        if sum_tax is not UNSET:
            field_dict["sumTax"] = sum_tax
        if sum_net_accounting is not UNSET:
            field_dict["sumNetAccounting"] = sum_net_accounting
        if sum_tax_accounting is not UNSET:
            field_dict["sumTaxAccounting"] = sum_tax_accounting
        if sum_gross_accounting is not UNSET:
            field_dict["sumGrossAccounting"] = sum_gross_accounting
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.voucher_pos_model_accounting_type import (
            VoucherPosModelAccountingType,
        )
        from ..models.voucher_pos_model_estimated_accounting_type import (
            VoucherPosModelEstimatedAccountingType,
        )
        from ..models.voucher_pos_model_sev_client import VoucherPosModelSevClient
        from ..models.voucher_pos_model_voucher import VoucherPosModelVoucher

        d = src_dict.copy()
        object_name = d.pop("objectName")

        map_all = d.pop("mapAll")

        accounting_type = VoucherPosModelAccountingType.from_dict(
            d.pop("accountingType")
        )

        tax_rate = d.pop("taxRate")

        net = d.pop("net")

        sum_net = d.pop("sumNet")

        sum_gross = d.pop("sumGross")

        id = d.pop("id", UNSET)

        create = d.pop("create", UNSET)

        update = d.pop("update", UNSET)

        _sev_client = d.pop("sevClient", UNSET)
        sev_client: Union[Unset, VoucherPosModelSevClient]
        if isinstance(_sev_client, Unset):
            sev_client = UNSET
        else:
            sev_client = VoucherPosModelSevClient.from_dict(_sev_client)

        _voucher = d.pop("voucher")
        voucher: Optional[VoucherPosModelVoucher]
        if _voucher is None:
            voucher = None
        else:
            voucher = VoucherPosModelVoucher.from_dict(_voucher)

        _estimated_accounting_type = d.pop("estimatedAccountingType", UNSET)
        estimated_accounting_type: Union[Unset, VoucherPosModelEstimatedAccountingType]
        if isinstance(_estimated_accounting_type, Unset):
            estimated_accounting_type = UNSET
        else:
            estimated_accounting_type = (
                VoucherPosModelEstimatedAccountingType.from_dict(
                    _estimated_accounting_type
                )
            )

        is_asset = d.pop("isAsset", UNSET)

        sum_tax = d.pop("sumTax", UNSET)

        sum_net_accounting = d.pop("sumNetAccounting", UNSET)

        sum_tax_accounting = d.pop("sumTaxAccounting", UNSET)

        sum_gross_accounting = d.pop("sumGrossAccounting", UNSET)

        comment = d.pop("comment", UNSET)

        voucher_pos_model = cls(
            object_name=object_name,
            map_all=map_all,
            accounting_type=accounting_type,
            tax_rate=tax_rate,
            net=net,
            sum_net=sum_net,
            sum_gross=sum_gross,
            id=id,
            create=create,
            update=update,
            sev_client=sev_client,
            voucher=voucher,
            estimated_accounting_type=estimated_accounting_type,
            is_asset=is_asset,
            sum_tax=sum_tax,
            sum_net_accounting=sum_net_accounting,
            sum_tax_accounting=sum_tax_accounting,
            sum_gross_accounting=sum_gross_accounting,
            comment=comment,
        )

        voucher_pos_model.additional_properties = d
        return voucher_pos_model

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
