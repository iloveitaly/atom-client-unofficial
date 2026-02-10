from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrailerData")


@_attrs_define
class TrailerData:
    """
    Attributes:
        trailer_urls (list[str] | Unset): List of trailer URLs
    """

    trailer_urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trailer_urls: list[str] | Unset = UNSET
        if not isinstance(self.trailer_urls, Unset):
            trailer_urls = self.trailer_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trailer_urls is not UNSET:
            field_dict["trailerUrls"] = trailer_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trailer_urls = cast(list[str], d.pop("trailerUrls", UNSET))

        trailer_data = cls(
            trailer_urls=trailer_urls,
        )

        trailer_data.additional_properties = d
        return trailer_data

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
