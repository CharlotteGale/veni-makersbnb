from lib.booking_repository import BookingRepository
from lib.booking import Booking

"""
When I call BookingRepository#create
I create a new Booking object in the seed data
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    new_booking = repo.create(Booking(None, 2, 3, '2026-01-20'))

    assert new_booking == Booking(3, 2, 3, '2026-01-20', 'pending')

"""
When we call BookingRepository#find_by_host
We get all bookings for listings owned by that host
"""
def test_find_by_host_returns_bookings_for_hosts_listings(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    # From your seed file, listing_id=2 belongs to user_id=2 (host 2)
    created = repo.create(Booking(None, 2, 3, '2026-01-20'))

    result = repo.find_by_host(2)

    assert result == [Booking(created.id, 2, 3, '2026-01-20', 'pending')]


"""
If the host has no bookings (or host doesn't exist),
find_by_host returns an empty list
"""
def test_find_by_host_returns_empty_list_if_no_bookings(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    result = repo.find_by_host(9999)

    assert result == []


def test_find_pending_requests_returns_pending_bookings_for_owners_listings_with_details(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    guest_row = db_connection.execute(
        "INSERT INTO users (email, password, name) VALUES (%s, %s, %s) RETURNING id;",
        ["guest@example.com", "hashedpw", "Guest One"]
    )
    guest_id = guest_row[0]["id"]

    created = repo.create(Booking(None, 2, guest_id, "2026-01-20", "pending"))

    result = repo.find_pending_requests(2)

    assert result == [
        {
            "id": created.id,
            "listing_id": 2,
            "guest_id": guest_id,
            "date": "2026-01-20",
            "status": "pending",
            "listing_name": "Shoreditch Loft Apartment",
            "guest_name": "Guest One",
            "guest_email": "guest@example.com",
        }
    ]


def test_find_pending_requests_returns_empty_list_if_none(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    assert repo.find_pending_requests(9999) == []
