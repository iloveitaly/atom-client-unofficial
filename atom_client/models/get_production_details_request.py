from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductionDetailsRequest")


@_attrs_define
class GetProductionDetailsRequest:
    """
    Attributes:
        ids (list[str]): List of production IDs
        marketplace_id (str | Unset): Marketplace identifier, defaults to 'US'
        page (int | Unset): Page number for pagination
        page_size (int | Unset): Number of items per page
    """

    ids: list[str]
    marketplace_id: str | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        marketplace_id = self.marketplace_id

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        marketplace_id = d.pop("marketplaceId", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        get_production_details_request = cls(
            ids=ids,
            marketplace_id=marketplace_id,
            page=page,
            page_size=page_size,
        )

        get_production_details_request.additional_properties = d
        return get_production_details_request

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
