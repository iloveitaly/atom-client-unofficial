from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_data import ImageData
    from ..models.trailer_data import TrailerData


T = TypeVar("T", bound="ProductionMedia")


@_attrs_define
class ProductionMedia:
    """
    Attributes:
        image_data (Union[Unset, ImageData]):
        trailer_data (Union[Unset, TrailerData]):
    """

    image_data: Union[Unset, "ImageData"] = UNSET
    trailer_data: Union[Unset, "TrailerData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image_data, Unset):
            image_data = self.image_data.to_dict()

        trailer_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trailer_data, Unset):
            trailer_data = self.trailer_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_data is not UNSET:
            field_dict["imageData"] = image_data
        if trailer_data is not UNSET:
            field_dict["trailerData"] = trailer_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_data import ImageData
        from ..models.trailer_data import TrailerData

        d = dict(src_dict)
        _image_data = d.pop("imageData", UNSET)
        image_data: Union[Unset, ImageData]
        if isinstance(_image_data, Unset):
            image_data = UNSET
        else:
            image_data = ImageData.from_dict(_image_data)

        _trailer_data = d.pop("trailerData", UNSET)
        trailer_data: Union[Unset, TrailerData]
        if isinstance(_trailer_data, Unset):
            trailer_data = UNSET
        else:
            trailer_data = TrailerData.from_dict(_trailer_data)

        production_media = cls(
            image_data=image_data,
            trailer_data=trailer_data,
        )

        production_media.additional_properties = d
        return production_media

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
