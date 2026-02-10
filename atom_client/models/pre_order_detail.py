from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreOrderDetail")


@_attrs_define
class PreOrderDetail:
    """
    Attributes:
        production_id (str | Unset): Associated production ID
        venue_id (str | Unset): Associated venue ID
        showtime_days (list[str] | Unset): List of pre-order showtime days
    """

    production_id: str | Unset = UNSET
    venue_id: str | Unset = UNSET
    showtime_days: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        production_id = self.production_id

        venue_id = self.venue_id

        showtime_days: list[str] | Unset = UNSET
        if not isinstance(self.showtime_days, Unset):
            showtime_days = self.showtime_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if production_id is not UNSET:
            field_dict["productionId"] = production_id
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if showtime_days is not UNSET:
            field_dict["showtimeDays"] = showtime_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        production_id = d.pop("productionId", UNSET)

        venue_id = d.pop("venueId", UNSET)

        showtime_days = cast(list[str], d.pop("showtimeDays", UNSET))

        pre_order_detail = cls(
            production_id=production_id,
            venue_id=venue_id,
            showtime_days=showtime_days,
        )

        pre_order_detail.additional_properties = d
        return pre_order_detail

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
