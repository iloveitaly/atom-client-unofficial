from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_info import PageInfo
    from ..models.venue_detail import VenueDetail


T = TypeVar("T", bound="VenueDetailsResponse")


@_attrs_define
class VenueDetailsResponse:
    """
    Attributes:
        venue_details (Union[Unset, list['VenueDetail']]): List of venue details
        page_info (Union[Unset, PageInfo]):
    """

    venue_details: Union[Unset, list["VenueDetail"]] = UNSET
    page_info: Union[Unset, "PageInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.venue_details, Unset):
            venue_details = []
            for venue_details_item_data in self.venue_details:
                venue_details_item = venue_details_item_data.to_dict()
                venue_details.append(venue_details_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if venue_details is not UNSET:
            field_dict["venueDetails"] = venue_details
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_info import PageInfo
        from ..models.venue_detail import VenueDetail

        d = dict(src_dict)
        venue_details = []
        _venue_details = d.pop("venueDetails", UNSET)
        for venue_details_item_data in _venue_details or []:
            venue_details_item = VenueDetail.from_dict(venue_details_item_data)

            venue_details.append(venue_details_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = PageInfo.from_dict(_page_info)

        venue_details_response = cls(
            venue_details=venue_details,
            page_info=page_info,
        )

        venue_details_response.additional_properties = d
        return venue_details_response

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
