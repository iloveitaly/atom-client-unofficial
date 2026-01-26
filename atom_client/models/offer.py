from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price import Price


T = TypeVar("T", bound="Offer")


@_attrs_define
class Offer:
    """
    Attributes:
        label (Union[Unset, str]): Offer label (e.g., "Ticket", "Child")
        price (Union[Unset, Price]):
    """

    label: Union[Unset, str] = UNSET
    price: Union[Unset, "Price"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price import Price

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, Price]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        offer = cls(
            label=label,
            price=price,
        )

        offer.additional_properties = d
        return offer

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
