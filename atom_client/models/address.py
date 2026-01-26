from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        line (Union[Unset, str]): Street address
        city (Union[Unset, str]): City
        state (Union[Unset, str]): State or province
        postal (Union[Unset, str]): Postal code
        lat (Union[Unset, float]): Latitude
        lon (Union[Unset, float]): Longitude
    """

    line: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    postal: Union[Unset, str] = UNSET
    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line = self.line

        city = self.city

        state = self.state

        postal = self.postal

        lat = self.lat

        lon = self.lon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal is not UNSET:
            field_dict["postal"] = postal
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line = d.pop("line", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal = d.pop("postal", UNSET)

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        address = cls(
            line=line,
            city=city,
            state=state,
            postal=postal,
            lat=lat,
            lon=lon,
        )

        address.additional_properties = d
        return address

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
