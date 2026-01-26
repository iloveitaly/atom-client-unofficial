import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_data import OfferData


T = TypeVar("T", bound="ShowtimeDetail")


@_attrs_define
class ShowtimeDetail:
    """
    Attributes:
        showtime_id (Union[Unset, str]): Unique showtime identifier
        production_id (Union[Unset, str]): Associated production ID
        venue_id (Union[Unset, str]): Associated venue ID
        offer_data (Union[Unset, OfferData]):
        utc_showtime_start (Union[Unset, datetime.datetime]): Showtime start in UTC, ISO8601 format without milliseconds
        local_showtime_start (Union[Unset, datetime.datetime]): Showtime start in local time, ISO8601 format
        attributes (Union[Unset, list[str]]): List of attribute keys referencing attributeMap
        checkout_url (Union[Unset, str]): URL for ticket checkout
        available_inventory (Union[Unset, int]): Number of available tickets
        tags (Union[Unset, list[str]]): Tags for special event showtimes
    """

    showtime_id: Union[Unset, str] = UNSET
    production_id: Union[Unset, str] = UNSET
    venue_id: Union[Unset, str] = UNSET
    offer_data: Union[Unset, "OfferData"] = UNSET
    utc_showtime_start: Union[Unset, datetime.datetime] = UNSET
    local_showtime_start: Union[Unset, datetime.datetime] = UNSET
    attributes: Union[Unset, list[str]] = UNSET
    checkout_url: Union[Unset, str] = UNSET
    available_inventory: Union[Unset, int] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        showtime_id = self.showtime_id

        production_id = self.production_id

        venue_id = self.venue_id

        offer_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.offer_data, Unset):
            offer_data = self.offer_data.to_dict()

        utc_showtime_start: Union[Unset, str] = UNSET
        if not isinstance(self.utc_showtime_start, Unset):
            utc_showtime_start = self.utc_showtime_start.isoformat(timespec="seconds")

        local_showtime_start: Union[Unset, str] = UNSET
        if not isinstance(self.local_showtime_start, Unset):
            local_showtime_start = self.local_showtime_start.isoformat(timespec="seconds")

        attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        checkout_url = self.checkout_url

        available_inventory = self.available_inventory

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if showtime_id is not UNSET:
            field_dict["showtimeId"] = showtime_id
        if production_id is not UNSET:
            field_dict["productionId"] = production_id
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if offer_data is not UNSET:
            field_dict["offerData"] = offer_data
        if utc_showtime_start is not UNSET:
            field_dict["utcShowtimeStart"] = utc_showtime_start
        if local_showtime_start is not UNSET:
            field_dict["localShowtimeStart"] = local_showtime_start
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if checkout_url is not UNSET:
            field_dict["checkoutUrl"] = checkout_url
        if available_inventory is not UNSET:
            field_dict["availableInventory"] = available_inventory
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offer_data import OfferData

        d = dict(src_dict)
        showtime_id = d.pop("showtimeId", UNSET)

        production_id = d.pop("productionId", UNSET)

        venue_id = d.pop("venueId", UNSET)

        _offer_data = d.pop("offerData", UNSET)
        offer_data: Union[Unset, OfferData]
        if isinstance(_offer_data, Unset):
            offer_data = UNSET
        else:
            offer_data = OfferData.from_dict(_offer_data)

        _utc_showtime_start = d.pop("utcShowtimeStart", UNSET)
        utc_showtime_start: Union[Unset, datetime.datetime]
        if isinstance(_utc_showtime_start, Unset):
            utc_showtime_start = UNSET
        else:
            utc_showtime_start = isoparse(_utc_showtime_start)

        _local_showtime_start = d.pop("localShowtimeStart", UNSET)
        local_showtime_start: Union[Unset, datetime.datetime]
        if isinstance(_local_showtime_start, Unset):
            local_showtime_start = UNSET
        else:
            local_showtime_start = isoparse(_local_showtime_start)

        attributes = cast(list[str], d.pop("attributes", UNSET))

        checkout_url = d.pop("checkoutUrl", UNSET)

        available_inventory = d.pop("availableInventory", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        showtime_detail = cls(
            showtime_id=showtime_id,
            production_id=production_id,
            venue_id=venue_id,
            offer_data=offer_data,
            utc_showtime_start=utc_showtime_start,
            local_showtime_start=local_showtime_start,
            attributes=attributes,
            checkout_url=checkout_url,
            available_inventory=available_inventory,
            tags=tags,
        )

        showtime_detail.additional_properties = d
        return showtime_detail

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
