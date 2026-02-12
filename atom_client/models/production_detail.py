from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contributors import Contributors
    from ..models.production_media import ProductionMedia


T = TypeVar("T", bound="ProductionDetail")


@_attrs_define
class ProductionDetail:
    """
    Attributes:
        id (str | Unset): Unique production identifier
        name (str | Unset): Production title
        production_media (ProductionMedia | Unset):
        contributors (Contributors | Unset):
        synopsis (str | Unset): Brief description of the production
        advisory_rating (str | Unset): Content advisory rating
        genres (list[str] | Unset): List of genres
        runtime_minutes (int | Unset): Runtime in minutes
        release_date (datetime.date | Unset): Release date in YYYY-MM-DD format
        atom_user_score (float | Unset): User score provided by Atom
        production_url (str | Unset): URL to the production's page
        distributor (str | Unset): Distributor of the production
        imdb_id (str | Unset): IMDb identifier
        atom_production_id (str | Unset): Atom-specific production identifier
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    production_media: ProductionMedia | Unset = UNSET
    contributors: Contributors | Unset = UNSET
    synopsis: str | Unset = UNSET
    advisory_rating: str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    runtime_minutes: int | Unset = UNSET
    release_date: datetime.date | Unset = UNSET
    atom_user_score: float | Unset = UNSET
    production_url: str | Unset = UNSET
    distributor: str | Unset = UNSET
    imdb_id: str | Unset = UNSET
    atom_production_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        production_media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.production_media, Unset):
            production_media = self.production_media.to_dict()

        contributors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contributors, Unset):
            contributors = self.contributors.to_dict()

        synopsis = self.synopsis

        advisory_rating = self.advisory_rating

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        runtime_minutes = self.runtime_minutes

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        atom_user_score = self.atom_user_score

        production_url = self.production_url

        distributor = self.distributor

        imdb_id = self.imdb_id

        atom_production_id = self.atom_production_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if production_media is not UNSET:
            field_dict["productionMedia"] = production_media
        if contributors is not UNSET:
            field_dict["contributors"] = contributors
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis
        if advisory_rating is not UNSET:
            field_dict["advisoryRating"] = advisory_rating
        if genres is not UNSET:
            field_dict["genres"] = genres
        if runtime_minutes is not UNSET:
            field_dict["runtimeMinutes"] = runtime_minutes
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if atom_user_score is not UNSET:
            field_dict["atomUserScore"] = atom_user_score
        if production_url is not UNSET:
            field_dict["productionUrl"] = production_url
        if distributor is not UNSET:
            field_dict["distributor"] = distributor
        if imdb_id is not UNSET:
            field_dict["imdbId"] = imdb_id
        if atom_production_id is not UNSET:
            field_dict["atomProductionId"] = atom_production_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contributors import Contributors
        from ..models.production_media import ProductionMedia

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _production_media = d.pop("productionMedia", UNSET)
        production_media: ProductionMedia | Unset
        if isinstance(_production_media, Unset):
            production_media = UNSET
        else:
            production_media = ProductionMedia.from_dict(_production_media)

        _contributors = d.pop("contributors", UNSET)
        contributors: Contributors | Unset
        if isinstance(_contributors, Unset):
            contributors = UNSET
        else:
            contributors = Contributors.from_dict(_contributors)

        synopsis = d.pop("synopsis", UNSET)

        advisory_rating = d.pop("advisoryRating", UNSET)

        genres = cast(list[str], d.pop("genres", UNSET))

        runtime_minutes = d.pop("runtimeMinutes", UNSET)

        _release_date = d.pop("releaseDate", UNSET)
        release_date: datetime.date | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        atom_user_score = d.pop("atomUserScore", UNSET)

        production_url = d.pop("productionUrl", UNSET)

        distributor = d.pop("distributor", UNSET)

        imdb_id = d.pop("imdbId", UNSET)

        atom_production_id = d.pop("atomProductionId", UNSET)

        production_detail = cls(
            id=id,
            name=name,
            production_media=production_media,
            contributors=contributors,
            synopsis=synopsis,
            advisory_rating=advisory_rating,
            genres=genres,
            runtime_minutes=runtime_minutes,
            release_date=release_date,
            atom_user_score=atom_user_score,
            production_url=production_url,
            distributor=distributor,
            imdb_id=imdb_id,
            atom_production_id=atom_production_id,
        )

        production_detail.additional_properties = d
        return production_detail

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
