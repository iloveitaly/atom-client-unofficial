from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.venue_details_response import VenueDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vendor_venue_id: str,
    *,
    circuit_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["circuitId"] = circuit_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partner/v1/venues/byVendorVenueId/{vendor_venue_id}".format(
            vendor_venue_id=quote(str(vendor_venue_id), safe=""),
        ),
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
    vendor_venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    circuit_id: str | Unset = UNSET,
) -> Response[VenueDetailsResponse]:
    """Query for venue by Vendor Venue ID

    Args:
        vendor_venue_id (str):
        circuit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VenueDetailsResponse]
    """

    kwargs = _get_kwargs(
        vendor_venue_id=vendor_venue_id,
        circuit_id=circuit_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vendor_venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    circuit_id: str | Unset = UNSET,
) -> VenueDetailsResponse | None:
    """Query for venue by Vendor Venue ID

    Args:
        vendor_venue_id (str):
        circuit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VenueDetailsResponse
    """

    return sync_detailed(
        vendor_venue_id=vendor_venue_id,
        client=client,
        circuit_id=circuit_id,
    ).parsed


async def asyncio_detailed(
    vendor_venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    circuit_id: str | Unset = UNSET,
) -> Response[VenueDetailsResponse]:
    """Query for venue by Vendor Venue ID

    Args:
        vendor_venue_id (str):
        circuit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VenueDetailsResponse]
    """

    kwargs = _get_kwargs(
        vendor_venue_id=vendor_venue_id,
        circuit_id=circuit_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vendor_venue_id: str,
    *,
    client: AuthenticatedClient | Client,
    circuit_id: str | Unset = UNSET,
) -> VenueDetailsResponse | None:
    """Query for venue by Vendor Venue ID

    Args:
        vendor_venue_id (str):
        circuit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VenueDetailsResponse
    """

    return (
        await asyncio_detailed(
            vendor_venue_id=vendor_venue_id,
            client=client,
            circuit_id=circuit_id,
        )
    ).parsed
