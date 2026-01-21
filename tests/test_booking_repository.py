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

    assert new_booking == Booking(1, 2, 3, '2026-01-20', 'pending')