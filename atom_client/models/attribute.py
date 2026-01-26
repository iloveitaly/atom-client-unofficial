from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attribute")


@_attrs_define
class Attribute:
    """
    Attributes:
        id (Union[Unset, str]): Unique attribute identifier
        type_ (Union[Unset, str]): Attribute type
        icon_url (Union[Unset, str]): URL to the attribute's icon
        friendly_name (Union[Unset, str]): Human-readable name of the attribute
        description (Union[Unset, str]): Description of the attribute
    """

    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        icon_url = self.icon_url

        friendly_name = self.friendly_name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        description = d.pop("description", UNSET)

        attribute = cls(
            id=id,
            type_=type_,
            icon_url=icon_url,
            friendly_name=friendly_name,
            description=description,
        )

        attribute.additional_properties = d
        return attribute

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
