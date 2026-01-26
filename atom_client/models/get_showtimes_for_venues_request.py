from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iso_date_bounds import ISODateBounds
    from ..models.local_date_bounds import LocalDateBounds


T = TypeVar("T", bound="GetShowtimesForVenuesRequest")


@_attrs_define
class GetShowtimesForVenuesRequest:
    """
    Attributes:
        venue_ids (list[str]): Set of venue IDs
        production_ids (Union[Unset, list[str]]): Optional set of production IDs to filter showtimes
        iso_date_bounds (Union[Unset, ISODateBounds]):
        local_date_bounds (Union[Unset, LocalDateBounds]):
        include_production_details (Union[Unset, bool]): Whether to include production details in the response
        marketplace_id (Union[Unset, str]): Optional marketplace identifier
    """

    venue_ids: list[str]
    production_ids: Union[Unset, list[str]] = UNSET
    iso_date_bounds: Union[Unset, "ISODateBounds"] = UNSET
    local_date_bounds: Union[Unset, "LocalDateBounds"] = UNSET
    include_production_details: Union[Unset, bool] = UNSET
    marketplace_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue_ids = self.venue_ids

        production_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.production_ids, Unset):
            production_ids = self.production_ids

        iso_date_bounds: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.iso_date_bounds, Unset):
            iso_date_bounds = self.iso_date_bounds.to_dict()

        local_date_bounds: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local_date_bounds, Unset):
            local_date_bounds = self.local_date_bounds.to_dict()

        include_production_details = self.include_production_details

        marketplace_id = self.marketplace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "venueIds": venue_ids,
            }
        )
        if production_ids is not UNSET:
            field_dict["productionIds"] = production_ids
        if iso_date_bounds is not UNSET:
            field_dict["isoDateBounds"] = iso_date_bounds
        if local_date_bounds is not UNSET:
            field_dict["localDateBounds"] = local_date_bounds
        if include_production_details is not UNSET:
            field_dict["includeProductionDetails"] = include_production_details
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iso_date_bounds import ISODateBounds
        from ..models.local_date_bounds import LocalDateBounds

        d = dict(src_dict)
        venue_ids = cast(list[str], d.pop("venueIds"))

        production_ids = cast(list[str], d.pop("productionIds", UNSET))

        _iso_date_bounds = d.pop("isoDateBounds", UNSET)
        iso_date_bounds: Union[Unset, ISODateBounds]
        if isinstance(_iso_date_bounds, Unset):
            iso_date_bounds = UNSET
        else:
            iso_date_bounds = ISODateBounds.from_dict(_iso_date_bounds)

        _local_date_bounds = d.pop("localDateBounds", UNSET)
        local_date_bounds: Union[Unset, LocalDateBounds]
        if isinstance(_local_date_bounds, Unset):
            local_date_bounds = UNSET
        else:
            local_date_bounds = LocalDateBounds.from_dict(_local_date_bounds)

        include_production_details = d.pop("includeProductionDetails", UNSET)

        marketplace_id = d.pop("marketplaceId", UNSET)

        get_showtimes_for_venues_request = cls(
            venue_ids=venue_ids,
            production_ids=production_ids,
            iso_date_bounds=iso_date_bounds,
            local_date_bounds=local_date_bounds,
            include_production_details=include_production_details,
            marketplace_id=marketplace_id,
        )

        get_showtimes_for_venues_request.additional_properties = d
        return get_showtimes_for_venues_request

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
