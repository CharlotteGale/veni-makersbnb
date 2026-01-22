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
        Booking(3, 3, 3, date(2026,4,14), 'confirmed'),
        Booking(4, 1, 3, date(2026,3,23), 'pending')
        ]

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

"""
When I call BookingRepository#check_dates
I can check if a date is available or not
"""
def test_check_date_availability(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    is_available = repo.check_dates(
        listing_id = 1,
        date = '2026-05-01'
    )

    assert is_available == True

    not_available = repo.check_dates(
        listing_id = 3,
        date = '2026-02-14'
    )

    assert not_available == False

    is_available_pending = repo.check_dates(
        listing_id = 1,
        date = '2026-03-01'
    )

    assert is_available_pending == True