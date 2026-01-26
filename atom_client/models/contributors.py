from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cast import Cast
    from ..models.crew import Crew


T = TypeVar("T", bound="Contributors")


@_attrs_define
class Contributors:
    """
    Attributes:
        cast (Union[Unset, list['Cast']]): List of cast members
        crew (Union[Unset, list['Crew']]): List of crew members
    """

    cast: Union[Unset, list["Cast"]] = UNSET
    crew: Union[Unset, list["Crew"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cast: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cast, Unset):
            cast = []
            for cast_item_data in self.cast:
                cast_item = cast_item_data.to_dict()
                cast.append(cast_item)

        crew: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.crew, Unset):
            crew = []
            for crew_item_data in self.crew:
                crew_item = crew_item_data.to_dict()
                crew.append(crew_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cast is not UNSET:
            field_dict["cast"] = cast
        if crew is not UNSET:
            field_dict["crew"] = crew

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cast import Cast
        from ..models.crew import Crew

        d = dict(src_dict)
        cast = []
        _cast = d.pop("cast", UNSET)
        for cast_item_data in _cast or []:
            cast_item = Cast.from_dict(cast_item_data)

            cast.append(cast_item)

        crew = []
        _crew = d.pop("crew", UNSET)
        for crew_item_data in _crew or []:
            crew_item = Crew.from_dict(crew_item_data)

            crew.append(crew_item)

        contributors = cls(
            cast=cast,
            crew=crew,
        )

        contributors.additional_properties = d
        return contributors

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
