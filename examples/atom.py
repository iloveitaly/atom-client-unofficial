"""
We decided not to use atom tickets anymore.

File ~/Projects/movie-tickets/atom-client/atom_client/api/default/get_partner_v_1_showtime_details_by_venue_venue_id.py:59, in _parse_response(client, response)
Unexpected Error Occurred: Invalid format: "2025-05-26T07:16:48" is too short
"""

from datetime import datetime
from typing import Any

from atom_client.api.default.get_partner_v_1_production_ids_by_venue_venue_id import (
    sync as get_production_ids_by_venue,
)
from atom_client.api.default.get_partner_v_1_showtime_details_by_venue_venue_id import (
    sync as get_venue_showtimes,
)
from atom_client.api.default.get_partner_v_1_venue_details_by_location import (
    sync as get_venues_by_location,
)
from atom_client.api.default.post_partner_v_1_production_details_by_ids import (
    sync as get_production_details_by_ids,
)
from atom_client.api.default.post_partner_v_1_venue_details_by_ids import (
    sync as get_venue_details_by_ids,
)
from atom_client.client import AuthenticatedClient
from atom_client.models.get_production_details_request import (
    GetProductionDetailsRequest,
)
from atom_client.models.get_venue_details_request import GetVenueDetailsRequest
from atom_client.models.showtime_detail import ShowtimeDetail
from atom_client.models.venue_detail import VenueDetail
from decouple import config
from pydantic import BaseModel
from whenever import Instant

from app import log

ATOM_API_BASE_URL = "https://api-beta.atomtickets.com"
ATOM_API_KEY = config("ATOM_API_KEY")


class AtomShowtime(BaseModel):
    """
    Converts an Atom Showtime object to a showtime object with just the information that we need

    Here's an empty object:

    ```
    ShowtimeDetailsResponse(showtime_details=[], pre_order_details=[], attribute_map=ShowtimeDetailsResponseAttributeMap(additional_properties={}), additional_properties={})
    ```

    pre_order_details seems to contain a list of days which a given showtime can preoder.

    ```
    ShowtimeDetail(
        showtime_id='D00589137483',
        production_id='B00110822522',
        venue_id='C00952957295',
        offer_data=OfferData(
            offers=[
                Offer(
                    label='General Admission',
                    price=<atom_client.types.Unset object at 0x10f3734d0>,
                    additional_properties={
                        'productId': '473511377GA',
                        'offerId': '250508-fbbb3f0c-e230-495b-9b5d-3ab34399f1bb',
                        'listPrice': 15.69,
                        'basePrice': 15.69,
                        'currency': 'USD',
                        'startDate': '2025-05-25T09:54:19.000Z',
                        'endDate': '2025-06-02T18:50:00.000Z',
                        'groupDiscount': {},
                        'taxExclusive': False,
                        'feeExclusive': True,
                        'feeAmount': 1.7,
                        'marketplaceId': 'US'
                    }
                )
            ],
            additional_properties={}
        ),
        utc_showtime_start=datetime.datetime(2025, 6, 2, 18, 40, tzinfo=tzutc()),
        local_showtime_start=datetime.datetime(2025, 6, 2, 14, 40, tzinfo=tzoffset(None, -14400)),
        attributes=['RESERVED'],
        checkout_url='http://rw-beta.atomtickets.com/checkout/redirect?productionId=B00110822522&venueId=C00952957295&localShowtime=2025-06-02T14:40:00&iref=atomapi',
        available_inventory=100,
        tags=<atom_client.types.Unset object at 0x10f3734d0>,
        additional_properties={'atomShowtimeId': '473511377', 'valid': True}
    )
    ```

    Some notes on the data structure:

    - local_showtime_end does not always exist
    - offer data does not always exist
    """

    id: str
    production_id: str
    venue_id: str

    # for now, I'm going to use the local times
    showtime_start: datetime

    price: float | None
    seats_available: int

    atom_redirect_url: str

    @classmethod
    def from_atom_showtime(cls, atom_showtime: ShowtimeDetail):
        # assertions about data structure

        # looks like there can sometimes be no offers
        assert len(atom_showtime.offer_data.offers) <= 1, (
            "multiple offers not supported"
        )

        # TODO should extract all other data we aren't using into a metadata field or something

        price = None

        if len(atom_showtime.offer_data.offers) == 1:
            offer = atom_showtime.offer_data.offers[0]

            # atom should be USA only, right?
            assert not hasattr(offer, "currency") or offer.currency == "USD", (
                "if currency is set, should be USD"
            )

            price = offer.price or offer.additional_properties["listPrice"]

        return cls(
            id=atom_showtime.showtime_id,
            production_id=atom_showtime.production_id,
            venue_id=atom_showtime.venue_id,
            showtime_start=atom_showtime.local_showtime_start,
            # showtime_end=atom_showtime.local_showtime_end,
            price=price,
            seats_available=atom_showtime.available_inventory,
            atom_redirect_url=atom_showtime.checkout_url,
        )


class AtomVenue(BaseModel):
    """
    Converts an Atom VenueDetail object to an AtomVenue object.

    Here's the data structure of a Atom Venue:

    VenueDetail(venue=Venue(id='C00695416726', name='AMC Empire 25', address=Address(line='234 West 42nd St.', city='New York', state='NY', postal='10036', lat=40.75645065307617, lon=-73.98885345458984, additional_properties={'country': 'US'}), properties=Properties(supports_concessions=True, supported=True, additional_properties={}), venue_url='http://rw-beta.atomtickets.com/theaters/redirect/C00695416726', atom_venue_id='7114', additional_properties={'atomVendorId': 'AMC'}), km_distance=0.09822911350315951, additional_properties={})
    """

    name: str
    address: str
    city: str
    state: str
    postal: str
    lat: float
    lon: float
    venue_url: str

    metadata: dict[str, Any]
    "additional data that we aren't sure if we need to store"

    atom_venue_alt_id: str
    "formatted like C00206845110"

    atom_venue_id: str
    "looks like a standard int, no alpha chars"

    showtimes: list[AtomShowtime] | None = None

    @classmethod
    def from_venue_detail(cls, venue_detail: VenueDetail):
        """Create an AtomVenue from a VenueDetail object."""
        venue = venue_detail.venue
        address = venue.address

        # Collect all additional properties into metadata
        metadata = {
            "km_distance": venue_detail.km_distance,
            "properties": venue.properties.to_dict() if venue.properties else {},
            "venue_additional_properties": venue.additional_properties or {},
            "venue_detail_additional_properties": venue_detail.additional_properties
            or {},
        }

        return cls(
            atom_venue_alt_id=venue.id,
            name=venue.name,
            address=address.line,
            city=address.city,
            state=address.state,
            postal=address.postal,
            lat=address.lat,
            lon=address.lon,
            venue_url=venue.venue_url,
            atom_venue_id=venue.atom_venue_id,
            metadata=metadata,
        )


def get_api_client() -> AuthenticatedClient:
    """Create an authenticated API client using the API key from environment variables."""
    client = AuthenticatedClient(base_url=ATOM_API_BASE_URL, token=ATOM_API_KEY)

    client.auth_header_name = "x-api-key"
    client.prefix = ""
    client.raise_on_unexpected_status = True

    return client


def fetch_venues_by_location(
    lat: float, lon: float, radius: int = 10
) -> list[AtomVenue]:
    """Fetch venues near the specified location."""
    client = get_api_client()
    response = get_venues_by_location(
        client=client, lat=lat, lon=lon, radius=radius, page=1, page_size=20
    )

    assert response

    venue_details = response.venue_details

    return [AtomVenue.from_venue_detail(venue_detail) for venue_detail in venue_details]


def fetch_showtimes_for_venue(venue: AtomVenue, client: AuthenticatedClient):
    """Fetch showtimes for a single venue.

    Args:
        venue: The venue to fetch showtimes for
        client: Authenticated API client

    Returns:
        Dictionary of showtimes if successful, None otherwise
    """
    log.info("fetching showtimes for venue", venue_name=venue.name)

    # for testing, lets use the current day to a month from now
    start_of_day = Instant.now().to_tz("UTC").start_of_day()
    end_date = start_of_day.add(days=30)

    showtimes = get_venue_showtimes(
        client=client,
        venue_id=str(venue.atom_venue_alt_id),  # Ensure venue.id is a string
        iso_start_date=start_of_day.py_datetime(),
        iso_end_date=end_date.py_datetime(),
    )

    assert showtimes

    return showtimes


def add_showtimes_to_venues(venues: list[AtomVenue]) -> dict:
    client = get_api_client()
    results = {}

    for venue in venues:
        showtimes = fetch_showtimes_for_venue(venue, client)

        if not showtimes.showtime_details:
            continue

        venue.showtimes = [
            AtomShowtime.from_atom_showtime(showtime)
            for showtime in showtimes.showtime_details
        ]

    return results


def get_venue_by_id(venue_id: str) -> AtomVenue:
    """Get the details of a venue."""
    client = get_api_client()

    venue_detail_response = get_venue_details_by_ids(
        client=client,
        body=GetVenueDetailsRequest(ids=[venue_id]),
    )

    assert venue_detail_response
    assert len(venue_detail_response.venue_details) == 1

    venue_detail = venue_detail_response.venue_details[0]

    venue = AtomVenue.from_venue_detail(venue_detail)
    showtimes = fetch_showtimes_for_venue(venue, client)

    if not showtimes.showtime_details:
        return venue

    venue.showtimes = [
        AtomShowtime.from_atom_showtime(showtime)
        for showtime in showtimes.showtime_details
    ]

    return venue


def get_showtimes_by_location(
    lat: float, lon: float, radius: int = 10
) -> list[AtomVenue]:
    """Get normalized showtimes for all venues near the specified location.

    Args:
        lat: Latitude of the location
        lon: Longitude of the location
        radius: Search radius in miles (default: 10)

    Returns:
        Dictionary mapping venue IDs to their showtimes
    """
    venues = fetch_venues_by_location(lat=lat, lon=lon, radius=radius)

    add_showtimes_to_venues(venues)

    return venues


def get_productions_by_venue(venue_id: str):
    """Get production IDs for a venue within the next 30 days.

    This won't be used in production, but is helpful for inspecting the atom API.

    Args:
        venue_id: The Atom venue ID to fetch productions for

    Returns:
        List of production IDs if successful, None otherwise
    """
    client = get_api_client()

    # Use current day to 30 days from now as the time range
    start_of_day = Instant.now().to_tz("UTC").start_of_day()
    end_date = start_of_day.add(days=30)

    production_response = get_production_ids_by_venue(
        client=client,
        venue_id=venue_id,
        iso_start_date=start_of_day.py_datetime(),
        iso_end_date=end_date.py_datetime(),
    )

    assert production_response

    production_ids = production_response.ids
    assert production_ids

    production_details_response = get_production_details_by_ids(
        client=client,
        body=GetProductionDetailsRequest(ids=production_ids),
    )

    return production_details_response
