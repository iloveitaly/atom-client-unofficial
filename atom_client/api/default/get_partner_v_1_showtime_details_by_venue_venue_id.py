import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.showtime_details_response import ShowtimeDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    venue_id: str,
    *,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    production_ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_iso_start_date: str | Unset = UNSET
    if not isinstance(iso_start_date, Unset):
        json_iso_start_date = iso_start_date.isoformat(timespec="seconds")
    params["isoStartDate"] = json_iso_start_date

    json_iso_end_date: str | Unset = UNSET
    if not isinstance(iso_end_date, Unset):
        json_iso_end_date = iso_end_date.isoformat(timespec="seconds")
    params["isoEndDate"] = json_iso_end_date

    params["localStartDate"] = local_start_date

    params["localEndDate"] = local_end_date

    params["productionIds"] = production_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partner/v1/showtime/details/byVenue/{venue_id}".format(
            venue_id=quote(str(venue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ShowtimeDetailsResponse | None:
    if response.status_code == 200:
        response_200 = ShowtimeDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ShowtimeDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    production_ids: str | Unset = UNSET,
) -> Response[ShowtimeDetailsResponse]:
    """Get showtimes for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Includes pre-order
    showtime data.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        production_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShowtimeDetailsResponse]
    """

    kwargs = _get_kwargs(
        venue_id=venue_id,
        iso_start_date=iso_start_date,
        iso_end_date=iso_end_date,
        local_start_date=local_start_date,
        local_end_date=local_end_date,
        production_ids=production_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    production_ids: str | Unset = UNSET,
) -> ShowtimeDetailsResponse | None:
    """Get showtimes for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Includes pre-order
    showtime data.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        production_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShowtimeDetailsResponse
    """

    return sync_detailed(
        venue_id=venue_id,
        client=client,
        iso_start_date=iso_start_date,
        iso_end_date=iso_end_date,
        local_start_date=local_start_date,
        local_end_date=local_end_date,
        production_ids=production_ids,
    ).parsed


async def asyncio_detailed(
    venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    production_ids: str | Unset = UNSET,
) -> Response[ShowtimeDetailsResponse]:
    """Get showtimes for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Includes pre-order
    showtime data.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        production_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShowtimeDetailsResponse]
    """

    kwargs = _get_kwargs(
        venue_id=venue_id,
        iso_start_date=iso_start_date,
        iso_end_date=iso_end_date,
        local_start_date=local_start_date,
        local_end_date=local_end_date,
        production_ids=production_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    production_ids: str | Unset = UNSET,
) -> ShowtimeDetailsResponse | None:
    """Get showtimes for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Includes pre-order
    showtime data.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        production_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShowtimeDetailsResponse
    """

    return (
        await asyncio_detailed(
            venue_id=venue_id,
            client=client,
            iso_start_date=iso_start_date,
            iso_end_date=iso_end_date,
            local_start_date=local_start_date,
            local_end_date=local_end_date,
            production_ids=production_ids,
        )
    ).parsed
