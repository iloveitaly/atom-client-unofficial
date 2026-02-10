from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pre_order_detail import PreOrderDetail
    from ..models.showtime_detail import ShowtimeDetail
    from ..models.showtime_details_response_attribute_map import ShowtimeDetailsResponseAttributeMap


T = TypeVar("T", bound="ShowtimeDetailsResponse")


@_attrs_define
class ShowtimeDetailsResponse:
    """
    Attributes:
        showtime_details (list[ShowtimeDetail] | Unset): List of showtime details
        pre_order_details (list[PreOrderDetail] | Unset): List of pre-order details
        attribute_map (ShowtimeDetailsResponseAttributeMap | Unset): Map of attribute keys to attribute details
    """

    showtime_details: list[ShowtimeDetail] | Unset = UNSET
    pre_order_details: list[PreOrderDetail] | Unset = UNSET
    attribute_map: ShowtimeDetailsResponseAttributeMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        showtime_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.showtime_details, Unset):
            showtime_details = []
            for showtime_details_item_data in self.showtime_details:
                showtime_details_item = showtime_details_item_data.to_dict()
                showtime_details.append(showtime_details_item)

        pre_order_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pre_order_details, Unset):
            pre_order_details = []
            for pre_order_details_item_data in self.pre_order_details:
                pre_order_details_item = pre_order_details_item_data.to_dict()
                pre_order_details.append(pre_order_details_item)

        attribute_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribute_map, Unset):
            attribute_map = self.attribute_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if showtime_details is not UNSET:
            field_dict["showtimeDetails"] = showtime_details
        if pre_order_details is not UNSET:
            field_dict["preOrderDetails"] = pre_order_details
        if attribute_map is not UNSET:
            field_dict["attributeMap"] = attribute_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pre_order_detail import PreOrderDetail
        from ..models.showtime_detail import ShowtimeDetail
        from ..models.showtime_details_response_attribute_map import ShowtimeDetailsResponseAttributeMap

        d = dict(src_dict)
        _showtime_details = d.pop("showtimeDetails", UNSET)
        showtime_details: list[ShowtimeDetail] | Unset = UNSET
        if _showtime_details is not UNSET:
            showtime_details = []
            for showtime_details_item_data in _showtime_details:
                showtime_details_item = ShowtimeDetail.from_dict(showtime_details_item_data)

                showtime_details.append(showtime_details_item)

        _pre_order_details = d.pop("preOrderDetails", UNSET)
        pre_order_details: list[PreOrderDetail] | Unset = UNSET
        if _pre_order_details is not UNSET:
            pre_order_details = []
            for pre_order_details_item_data in _pre_order_details:
                pre_order_details_item = PreOrderDetail.from_dict(pre_order_details_item_data)

                pre_order_details.append(pre_order_details_item)

        _attribute_map = d.pop("attributeMap", UNSET)
        attribute_map: ShowtimeDetailsResponseAttributeMap | Unset
        if isinstance(_attribute_map, Unset):
            attribute_map = UNSET
        else:
            attribute_map = ShowtimeDetailsResponseAttributeMap.from_dict(_attribute_map)

        showtime_details_response = cls(
            showtime_details=showtime_details,
            pre_order_details=pre_order_details,
            attribute_map=attribute_map,
        )

        showtime_details_response.additional_properties = d
        return showtime_details_response

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
