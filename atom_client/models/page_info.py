from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageInfo")


@_attrs_define
class PageInfo:
    """
    Attributes:
        page (int | Unset): Current page number
        page_size (int | Unset): Number of items per page
        total_pages (int | Unset): Total number of pages
    """

    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        page_info = cls(
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

        page_info.additional_properties = d
        return page_info

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
