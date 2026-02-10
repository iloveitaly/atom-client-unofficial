import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.production_ids_response import ProductionIdsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    venue_id: str,
    *,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    marketplace_id: str | Unset = UNSET,
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

    params["marketplaceId"] = marketplace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partner/v1/production/ids/byVenue/{venue_id}".format(
            venue_id=quote(str(venue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProductionIdsResponse | None:
    if response.status_code == 200:
        response_200 = ProductionIdsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProductionIdsResponse]:
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
    marketplace_id: str | Unset = UNSET,
) -> Response[ProductionIdsResponse]:
    """Get production IDs for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Results ordered by
    Atom Meter.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        marketplace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductionIdsResponse]
    """

    kwargs = _get_kwargs(
        venue_id=venue_id,
        iso_start_date=iso_start_date,
        iso_end_date=iso_end_date,
        local_start_date=local_start_date,
        local_end_date=local_end_date,
        marketplace_id=marketplace_id,
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
    marketplace_id: str | Unset = UNSET,
) -> ProductionIdsResponse | None:
    """Get production IDs for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Results ordered by
    Atom Meter.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        marketplace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductionIdsResponse
    """

    return sync_detailed(
        venue_id=venue_id,
        client=client,
        iso_start_date=iso_start_date,
        iso_end_date=iso_end_date,
        local_start_date=local_start_date,
        local_end_date=local_end_date,
        marketplace_id=marketplace_id,
    ).parsed


async def asyncio_detailed(
    venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    iso_start_date: datetime.datetime | Unset = UNSET,
    iso_end_date: datetime.datetime | Unset = UNSET,
    local_start_date: str | Unset = UNSET,
    local_end_date: str | Unset = UNSET,
    marketplace_id: str | Unset = UNSET,
) -> Response[ProductionIdsResponse]:
    """Get production IDs for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Results ordered by
    Atom Meter.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        marketplace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductionIdsResponse]
    """

    kwargs = _get_kwargs(
        venue_id=venue_id,
        iso_start_date=iso_start_date,
        iso_end_date=iso_end_date,
        local_start_date=local_start_date,
        local_end_date=local_end_date,
        marketplace_id=marketplace_id,
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
    marketplace_id: str | Unset = UNSET,
) -> ProductionIdsResponse | None:
    """Get production IDs for a venue within a date range

     Requires either isoStartDate and isoEndDate, or localStartDate and localEndDate. Results ordered by
    Atom Meter.

    Args:
        venue_id (str):
        iso_start_date (datetime.datetime | Unset):
        iso_end_date (datetime.datetime | Unset):
        local_start_date (str | Unset):
        local_end_date (str | Unset):
        marketplace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductionIdsResponse
    """

    return (
        await asyncio_detailed(
            venue_id=venue_id,
            client=client,
            iso_start_date=iso_start_date,
            iso_end_date=iso_end_date,
            local_start_date=local_start_date,
            local_end_date=local_end_date,
            marketplace_id=marketplace_id,
        )
    ).parsed
