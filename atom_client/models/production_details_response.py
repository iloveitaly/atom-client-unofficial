from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_info import PageInfo
    from ..models.production_detail import ProductionDetail


T = TypeVar("T", bound="ProductionDetailsResponse")


@_attrs_define
class ProductionDetailsResponse:
    """
    Attributes:
        production_details (list[ProductionDetail] | Unset): List of production details
        page_info (PageInfo | Unset):
    """

    production_details: list[ProductionDetail] | Unset = UNSET
    page_info: PageInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        production_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.production_details, Unset):
            production_details = []
            for production_details_item_data in self.production_details:
                production_details_item = production_details_item_data.to_dict()
                production_details.append(production_details_item)

        page_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if production_details is not UNSET:
            field_dict["productionDetails"] = production_details
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_info import PageInfo
        from ..models.production_detail import ProductionDetail

        d = dict(src_dict)
        _production_details = d.pop("productionDetails", UNSET)
        production_details: list[ProductionDetail] | Unset = UNSET
        if _production_details is not UNSET:
            production_details = []
            for production_details_item_data in _production_details:
                production_details_item = ProductionDetail.from_dict(production_details_item_data)

                production_details.append(production_details_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: PageInfo | Unset
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = PageInfo.from_dict(_page_info)

        production_details_response = cls(
            production_details=production_details,
            page_info=page_info,
        )

        production_details_response.additional_properties = d
        return production_details_response

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
