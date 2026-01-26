from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.venue_details_response import VenueDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    term: str,
    lat: float,
    lon: float,
    radius: float,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["term"] = term

    params["lat"] = lat

    params["lon"] = lon

    params["radius"] = radius

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partner/v1/venue/details/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VenueDetailsResponse]:
    if response.status_code == 200:
        response_200 = VenueDetailsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VenueDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    lat: float,
    lon: float,
    radius: float,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[VenueDetailsResponse]:
    """Query for venues by name

    Args:
        term (str):
        lat (float):
        lon (float):
        radius (float):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VenueDetailsResponse]
    """

    kwargs = _get_kwargs(
        term=term,
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
    client: Union[AuthenticatedClient, Client],
    term: str,
    lat: float,
    lon: float,
    radius: float,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[VenueDetailsResponse]:
    """Query for venues by name

    Args:
        term (str):
        lat (float):
        lon (float):
        radius (float):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VenueDetailsResponse
    """

    return sync_detailed(
        client=client,
        term=term,
        lat=lat,
        lon=lon,
        radius=radius,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    lat: float,
    lon: float,
    radius: float,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[VenueDetailsResponse]:
    """Query for venues by name

    Args:
        term (str):
        lat (float):
        lon (float):
        radius (float):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VenueDetailsResponse]
    """

    kwargs = _get_kwargs(
        term=term,
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
    client: Union[AuthenticatedClient, Client],
    term: str,
    lat: float,
    lon: float,
    radius: float,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[VenueDetailsResponse]:
    """Query for venues by name

    Args:
        term (str):
        lat (float):
        lon (float):
        radius (float):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VenueDetailsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            term=term,
            lat=lat,
            lon=lon,
            radius=radius,
            page=page,
            page_size=page_size,
        )
    ).parsed
