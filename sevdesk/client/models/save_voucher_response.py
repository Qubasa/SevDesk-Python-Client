from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.voucher_pos_response_model import VoucherPosResponseModel
    from ..models.voucher_response_model import VoucherResponseModel


T = TypeVar("T", bound="SaveVoucherResponse")


@attr.s(auto_attribs=True)
class SaveVoucherResponse:
    """
    Attributes:
        voucher (Union[Unset, VoucherResponseModel]): Voucher model
        voucher_pos (Union[Unset, List['VoucherPosResponseModel']]):
        filename (Union[Unset, File]): Filename of a previously upload file which should be attached.
    """

    voucher: Union[Unset, "VoucherResponseModel"] = UNSET
    voucher_pos: Union[Unset, List["VoucherPosResponseModel"]] = UNSET
    filename: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voucher: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voucher, Unset):
            voucher = self.voucher.to_dict()

        voucher_pos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.voucher_pos, Unset):
            voucher_pos = []
            for voucher_pos_item_data in self.voucher_pos:
                voucher_pos_item = voucher_pos_item_data.to_dict()

                voucher_pos.append(voucher_pos_item)

        filename: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.filename, Unset):
            filename = self.filename.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voucher is not UNSET:
            field_dict["voucher"] = voucher
        if voucher_pos is not UNSET:
            field_dict["voucherPos"] = voucher_pos
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.voucher_pos_response_model import VoucherPosResponseModel
        from ..models.voucher_response_model import VoucherResponseModel

        d = src_dict.copy()
        _voucher = d.pop("voucher", UNSET)
        voucher: Union[Unset, VoucherResponseModel]
        if isinstance(_voucher, Unset):
            voucher = UNSET
        else:
            voucher = VoucherResponseModel.from_dict(_voucher)

        voucher_pos = []
        _voucher_pos = d.pop("voucherPos", UNSET)
        for voucher_pos_item_data in _voucher_pos or []:
            voucher_pos_item = VoucherPosResponseModel.from_dict(voucher_pos_item_data)

            voucher_pos.append(voucher_pos_item)

        _filename = d.pop("filename", UNSET)
        filename: Union[Unset, File]
        if isinstance(_filename, Unset):
            filename = UNSET
        else:
            filename = File(payload=BytesIO(_filename))

        save_voucher_response = cls(
            voucher=voucher,
            voucher_pos=voucher_pos,
            filename=filename,
        )

        save_voucher_response.additional_properties = d
        return save_voucher_response

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
