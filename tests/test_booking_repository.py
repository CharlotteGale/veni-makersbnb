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
        Booking(3, 3, 3, date(2026,2,14), 'confirmed'),
        Booking(4, 1, 3, date(2026,3,23), 'pending')
        ]

