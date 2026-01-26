import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ISODateBounds")


@_attrs_define
class ISODateBounds:
    """
    Attributes:
        iso_start_date (Union[Unset, datetime.datetime]): Start date in ISO8601 format without milliseconds
        iso_end_date (Union[Unset, datetime.datetime]): End date in ISO8601 format without milliseconds
    """

    iso_start_date: Union[Unset, datetime.datetime] = UNSET
    iso_end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iso_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.iso_start_date, Unset):
            iso_start_date = self.iso_start_date.isoformat(timespec="seconds")

        iso_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.iso_end_date, Unset):
            iso_end_date = self.iso_end_date.isoformat(timespec="seconds")

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iso_start_date is not UNSET:
            field_dict["isoStartDate"] = iso_start_date
        if iso_end_date is not UNSET:
            field_dict["isoEndDate"] = iso_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _iso_start_date = d.pop("isoStartDate", UNSET)
        iso_start_date: Union[Unset, datetime.datetime]
        if isinstance(_iso_start_date, Unset):
            iso_start_date = UNSET
        else:
            iso_start_date = isoparse(_iso_start_date)

        _iso_end_date = d.pop("isoEndDate", UNSET)
        iso_end_date: Union[Unset, datetime.datetime]
        if isinstance(_iso_end_date, Unset):
            iso_end_date = UNSET
        else:
            iso_end_date = isoparse(_iso_end_date)

        iso_date_bounds = cls(
            iso_start_date=iso_start_date,
            iso_end_date=iso_end_date,
        )

        iso_date_bounds.additional_properties = d
        return iso_date_bounds

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
