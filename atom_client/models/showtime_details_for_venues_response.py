from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.showtime_details_for_venues_response_attribute_map import ShowtimeDetailsForVenuesResponseAttributeMap
    from ..models.showtime_details_for_venues_response_production_details_map import (
        ShowtimeDetailsForVenuesResponseProductionDetailsMap,
    )
    from ..models.showtime_details_for_venues_response_venue_showtime_details_map import (
        ShowtimeDetailsForVenuesResponseVenueShowtimeDetailsMap,
    )


T = TypeVar("T", bound="ShowtimeDetailsForVenuesResponse")


@_attrs_define
class ShowtimeDetailsForVenuesResponse:
    """
    Attributes:
        venue_showtime_details_map (Union[Unset, ShowtimeDetailsForVenuesResponseVenueShowtimeDetailsMap]): Map of venue
            IDs to their showtime details
        attribute_map (Union[Unset, ShowtimeDetailsForVenuesResponseAttributeMap]): Map of attribute keys to attribute
            details
        production_details_map (Union[Unset, ShowtimeDetailsForVenuesResponseProductionDetailsMap]): Map of production
            IDs to production details
    """

    venue_showtime_details_map: Union[Unset, "ShowtimeDetailsForVenuesResponseVenueShowtimeDetailsMap"] = UNSET
    attribute_map: Union[Unset, "ShowtimeDetailsForVenuesResponseAttributeMap"] = UNSET
    production_details_map: Union[Unset, "ShowtimeDetailsForVenuesResponseProductionDetailsMap"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue_showtime_details_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue_showtime_details_map, Unset):
            venue_showtime_details_map = self.venue_showtime_details_map.to_dict()

        attribute_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute_map, Unset):
            attribute_map = self.attribute_map.to_dict()

        production_details_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.production_details_map, Unset):
            production_details_map = self.production_details_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if venue_showtime_details_map is not UNSET:
            field_dict["venueShowtimeDetailsMap"] = venue_showtime_details_map
        if attribute_map is not UNSET:
            field_dict["attributeMap"] = attribute_map
        if production_details_map is not UNSET:
            field_dict["productionDetailsMap"] = production_details_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.showtime_details_for_venues_response_attribute_map import (
            ShowtimeDetailsForVenuesResponseAttributeMap,
        )
        from ..models.showtime_details_for_venues_response_production_details_map import (
            ShowtimeDetailsForVenuesResponseProductionDetailsMap,
        )
        from ..models.showtime_details_for_venues_response_venue_showtime_details_map import (
            ShowtimeDetailsForVenuesResponseVenueShowtimeDetailsMap,
        )

        d = dict(src_dict)
        _venue_showtime_details_map = d.pop("venueShowtimeDetailsMap", UNSET)
        venue_showtime_details_map: Union[Unset, ShowtimeDetailsForVenuesResponseVenueShowtimeDetailsMap]
        if isinstance(_venue_showtime_details_map, Unset):
            venue_showtime_details_map = UNSET
        else:
            venue_showtime_details_map = ShowtimeDetailsForVenuesResponseVenueShowtimeDetailsMap.from_dict(
                _venue_showtime_details_map
            )

        _attribute_map = d.pop("attributeMap", UNSET)
        attribute_map: Union[Unset, ShowtimeDetailsForVenuesResponseAttributeMap]
        if isinstance(_attribute_map, Unset):
            attribute_map = UNSET
        else:
            attribute_map = ShowtimeDetailsForVenuesResponseAttributeMap.from_dict(_attribute_map)

        _production_details_map = d.pop("productionDetailsMap", UNSET)
        production_details_map: Union[Unset, ShowtimeDetailsForVenuesResponseProductionDetailsMap]
        if isinstance(_production_details_map, Unset):
            production_details_map = UNSET
        else:
            production_details_map = ShowtimeDetailsForVenuesResponseProductionDetailsMap.from_dict(
                _production_details_map
            )

        showtime_details_for_venues_response = cls(
            venue_showtime_details_map=venue_showtime_details_map,
            attribute_map=attribute_map,
            production_details_map=production_details_map,
        )

        showtime_details_for_venues_response.additional_properties = d
        return showtime_details_for_venues_response

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
