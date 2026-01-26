from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.venue import Venue


T = TypeVar("T", bound="VenueDetail")


@_attrs_define
class VenueDetail:
    """
    Attributes:
        venue (Union[Unset, Venue]):
        km_distance (Union[Unset, float]): Distance in kilometers from the specified location
    """

    venue: Union[Unset, "Venue"] = UNSET
    km_distance: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        km_distance = self.km_distance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if venue is not UNSET:
            field_dict["venue"] = venue
        if km_distance is not UNSET:
            field_dict["kmDistance"] = km_distance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.venue import Venue

        d = dict(src_dict)
        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, Venue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = Venue.from_dict(_venue)

        km_distance = d.pop("kmDistance", UNSET)

        venue_detail = cls(
            venue=venue,
            km_distance=km_distance,
        )

        venue_detail.additional_properties = d
        return venue_detail

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
