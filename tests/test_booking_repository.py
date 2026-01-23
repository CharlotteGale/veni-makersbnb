from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date

"""
When I call BookingRepository#create
I create a new Booking object in the seed data
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    new_booking = repo.create(Booking(None, 2, 8, '2026-01-20'))

    assert new_booking == Booking(1, 2, 3, '2026-01-20', 'pending')

"""
When I call BookingRepository#create
I create a new Booking object in the seed data
"""

def test_read_all_records(db_connection):
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
    assert repo.all() == [new_booking]
    assert new_booking == Booking(3, 2, 3, '2026-01-20', 'pending')
    assert new_booking == Booking(5, 2, 8, '2026-01-20', 'pending')


"""
When I call BookingRepository#show_guest_bookings
I show only the bookings for that guest. 
"""

def test_show_guest_bookings(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    search_results = repo.show_guest_bookings(3)

    assert search_results == [
        Booking(3, 3, 3, date(2026,2,14), 'confirmed',"Countryside Barn Retreat","Peaceful converted barn with countryside walks, a wood burner, and beautiful sunset views.",140), #listing id (2nd pos) = 3
        Booking(4, 1, 3, date(2026,3,23), 'pending',"Cozy Canal Studio", "Bright studio with canal views, fast WiFi, and a comfy queen bed — perfect for a weekend escape.", 95)
        ]  #listing id (2nd pos) = 1


"""
When I call BookingRepository#confirm_booking
I update the status to confirmed
"""
def test_update_booking_status_to_confirmed(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    repo.create(Booking(None, 6, 3, '2026-03-01'))

    repo.confirm_booking(3)

    result = db_connection.execute('SELECT status FROM bookings WHERE id = %s;', [3])
    assert result[0]['status'] == 'confirmed'


"""
When I call BookingRepository#reject_booking
I update the status to rejected
"""
def test_update_booking_status_to_rejected(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    repo.create(Booking(None, 6, 3, '2026-03-01'))

    repo.reject_booking(3)

    result = db_connection.execute('SELECT status FROM bookings WHERE id = %s;', [3])
    assert result[0]['status'] == 'rejected'

