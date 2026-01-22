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

"""
When I call BookingRepository#create
I create a new Booking object in the seed data
"""

def test_read_all_records(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    new_booking = repo.create(Booking(None, 2, 3, '2026-01-20'))

    assert repo.all() == [new_booking]
    assert new_booking == Booking(3, 2, 3, '2026-01-20', 'pending')

"""
When I call BookingRepository#update_status
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
When I call BookingRepository#update_status
I update the status to rejected
"""
def test_update_booking_status_to_rejected(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = BookingRepository(db_connection)

    repo.create(Booking(None, 6, 3, '2026-03-01'))

    repo.reject_booking(3)

    result = db_connection.execute('SELECT status FROM bookings WHERE id = %s;', [3])
    assert result[0]['status'] == 'rejected'
