from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageData")


@_attrs_define
class ImageData:
    """
    Attributes:
        cover_image_url (Union[Unset, str]): URL to the cover image
        promo_image_urls (Union[Unset, list[str]]): List of promotional image URLs
    """

    cover_image_url: Union[Unset, str] = UNSET
    promo_image_urls: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_image_url = self.cover_image_url

        promo_image_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.promo_image_urls, Unset):
            promo_image_urls = self.promo_image_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_image_url is not UNSET:
            field_dict["coverImageUrl"] = cover_image_url
        if promo_image_urls is not UNSET:
            field_dict["promoImageUrls"] = promo_image_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover_image_url = d.pop("coverImageUrl", UNSET)

        promo_image_urls = cast(list[str], d.pop("promoImageUrls", UNSET))

        image_data = cls(
            cover_image_url=cover_image_url,
            promo_image_urls=promo_image_urls,
        )

        image_data.additional_properties = d
        return image_data

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
