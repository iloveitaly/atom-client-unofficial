from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer import Offer


T = TypeVar("T", bound="OfferData")


@_attrs_define
class OfferData:
    """
    Attributes:
        offers (list[Offer] | Unset): List of pricing offers
    """

    offers: list[Offer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offers is not UNSET:
            field_dict["offers"] = offers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offer import Offer

        d = dict(src_dict)
        _offers = d.pop("offers", UNSET)
        offers: list[Offer] | Unset = UNSET
        if _offers is not UNSET:
            offers = []
            for offers_item_data in _offers:
                offers_item = Offer.from_dict(offers_item_data)

                offers.append(offers_item)

        offer_data = cls(
            offers=offers,
        )

        offer_data.additional_properties = d
        return offer_data

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
