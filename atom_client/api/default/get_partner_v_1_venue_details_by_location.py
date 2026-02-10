from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.venue_details_response import VenueDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lat: float,
    lon: float,
    radius: float,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lat"] = lat

    params["lon"] = lon

    params["radius"] = radius

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partner/v1/venue/details/byLocation",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> VenueDetailsResponse | None:
    if response.status_code == 200:
        response_200 = VenueDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[VenueDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
    radius: float,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[VenueDetailsResponse]:
    """Query for venues by location

    Args:
        lat (float):
        lon (float):
        radius (float):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VenueDetailsResponse]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
        radius=radius,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
    radius: float,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> VenueDetailsResponse | None:
    """Query for venues by location

    Args:
        lat (float):
        lon (float):
        radius (float):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VenueDetailsResponse
    """

    return sync_detailed(
        client=client,
        lat=lat,
        lon=lon,
        radius=radius,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
    radius: float,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[VenueDetailsResponse]:
    """Query for venues by location

    Args:
        lat (float):
        lon (float):
        radius (float):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VenueDetailsResponse]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
        radius=radius,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
    radius: float,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> VenueDetailsResponse | None:
    """Query for venues by location

    Args:
        lat (float):
        lon (float):
        radius (float):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VenueDetailsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            lon=lon,
            radius=radius,
            page=page,
            page_size=page_size,
        )
    ).parsed
