from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalDateBounds")


@_attrs_define
class LocalDateBounds:
    """
    Attributes:
        local_start_date (Union[Unset, str]): Start date in YYYY-MM-DDTHH:MM:SS format (no timezone)
        local_end_date (Union[Unset, str]): End date in YYYY-MM-DDTHH:MM:SS format (no timezone)
    """

    local_start_date: Union[Unset, str] = UNSET
    local_end_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_start_date = self.local_start_date

        local_end_date = self.local_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_start_date is not UNSET:
            field_dict["localStartDate"] = local_start_date
        if local_end_date is not UNSET:
            field_dict["localEndDate"] = local_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        local_start_date = d.pop("localStartDate", UNSET)

        local_end_date = d.pop("localEndDate", UNSET)

        local_date_bounds = cls(
            local_start_date=local_start_date,
            local_end_date=local_end_date,
        )

        local_date_bounds.additional_properties = d
        return local_date_bounds

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
