from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_voucher_by_factory_json_body_voucher_pos_delete import (
        CreateVoucherByFactoryJsonBodyVoucherPosDelete,
    )
    from ..models.voucher_model import VoucherModel
    from ..models.voucher_pos_model import VoucherPosModel


T = TypeVar("T", bound="CreateVoucherByFactoryJsonBody")


@attr.s(auto_attribs=True)
class CreateVoucherByFactoryJsonBody:
    """
    Attributes:
        voucher (VoucherModel): Voucher model
        voucher_pos_save (Union[Unset, List['VoucherPosModel']]):
        voucher_pos_delete (Union[Unset, CreateVoucherByFactoryJsonBodyVoucherPosDelete]):
        filename (Union[Unset, str]): Filename of a previously upload file which should be attached.
    """

    voucher: "VoucherModel"
    voucher_pos_save: Union[Unset, List["VoucherPosModel"]] = UNSET
    voucher_pos_delete: Union[
        Unset, "CreateVoucherByFactoryJsonBodyVoucherPosDelete"
    ] = UNSET
    filename: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voucher = self.voucher.to_dict()

        voucher_pos_save: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.voucher_pos_save, Unset):
            voucher_pos_save = []
            for voucher_pos_save_item_data in self.voucher_pos_save:
                voucher_pos_save_item = voucher_pos_save_item_data.to_dict()

                voucher_pos_save.append(voucher_pos_save_item)

        voucher_pos_delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voucher_pos_delete, Unset):
            voucher_pos_delete = self.voucher_pos_delete.to_dict()

        filename = self.filename

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voucher": voucher,
            }
        )
        if voucher_pos_save is not UNSET:
            field_dict["voucherPosSave"] = voucher_pos_save
        if voucher_pos_delete is not UNSET:
            field_dict["voucherPosDelete"] = voucher_pos_delete
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_voucher_by_factory_json_body_voucher_pos_delete import (
            CreateVoucherByFactoryJsonBodyVoucherPosDelete,
        )
        from ..models.voucher_model import VoucherModel
        from ..models.voucher_pos_model import VoucherPosModel

        d = src_dict.copy()
        voucher = VoucherModel.from_dict(d.pop("voucher"))

        voucher_pos_save = []
        _voucher_pos_save = d.pop("voucherPosSave", UNSET)
        for voucher_pos_save_item_data in _voucher_pos_save or []:
            voucher_pos_save_item = VoucherPosModel.from_dict(
                voucher_pos_save_item_data
            )

            voucher_pos_save.append(voucher_pos_save_item)

        _voucher_pos_delete = d.pop("voucherPosDelete", UNSET)
        voucher_pos_delete: Union[Unset, CreateVoucherByFactoryJsonBodyVoucherPosDelete]
        if isinstance(_voucher_pos_delete, Unset):
            voucher_pos_delete = UNSET
        else:
            voucher_pos_delete = (
                CreateVoucherByFactoryJsonBodyVoucherPosDelete.from_dict(
                    _voucher_pos_delete
                )
            )

        filename = d.pop("filename", UNSET)

        create_voucher_by_factory_json_body = cls(
            voucher=voucher,
            voucher_pos_save=voucher_pos_save,
            voucher_pos_delete=voucher_pos_delete,
            filename=filename,
        )

        create_voucher_by_factory_json_body.additional_properties = d
        return create_voucher_by_factory_json_body

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
