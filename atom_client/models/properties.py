from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Properties")


@_attrs_define
class Properties:
    """
    Attributes:
        supports_concessions (bool | Unset): Whether the venue supports concessions
        supported (bool | Unset): Whether the venue is supported by Atom Tickets
    """

    supports_concessions: bool | Unset = UNSET
    supported: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supports_concessions = self.supports_concessions

        supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supports_concessions is not UNSET:
            field_dict["supportsConcessions"] = supports_concessions
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supports_concessions = d.pop("supportsConcessions", UNSET)

        supported = d.pop("supported", UNSET)

        properties = cls(
            supports_concessions=supports_concessions,
            supported=supported,
        )

        properties.additional_properties = d
        return properties

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
