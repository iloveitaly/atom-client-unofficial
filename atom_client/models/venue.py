from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.properties import Properties


T = TypeVar("T", bound="Venue")


@_attrs_define
class Venue:
    """
    Attributes:
        id (str | Unset): Unique venue identifier
        name (str | Unset): Venue name
        address (Address | Unset):
        properties (Properties | Unset):
        venue_url (str | Unset): URL to the venue's page
        atom_venue_id (str | Unset): Atom-specific venue identifier
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    address: Address | Unset = UNSET
    properties: Properties | Unset = UNSET
    venue_url: str | Unset = UNSET
    atom_venue_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        venue_url = self.venue_url

        atom_venue_id = self.atom_venue_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if properties is not UNSET:
            field_dict["properties"] = properties
        if venue_url is not UNSET:
            field_dict["venueUrl"] = venue_url
        if atom_venue_id is not UNSET:
            field_dict["atomVenueId"] = atom_venue_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.properties import Properties

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        _properties = d.pop("properties", UNSET)
        properties: Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = Properties.from_dict(_properties)

        venue_url = d.pop("venueUrl", UNSET)

        atom_venue_id = d.pop("atomVenueId", UNSET)

        venue = cls(
            id=id,
            name=name,
            address=address,
            properties=properties,
            venue_url=venue_url,
            atom_venue_id=atom_venue_id,
        )

        venue.additional_properties = d
        return venue

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
