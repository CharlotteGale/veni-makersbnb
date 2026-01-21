from lib.booking import Booking
"""
Ensure Booking object constructs
"""
def test_booking_constructs():
    booking = Booking(1, 2, 3, '2026-01-20')

    assert booking.id == 1
    assert booking.listing_id == 2
    assert booking.guest_id == 3
    assert booking.date == '2026-01-20'
    assert booking.status == 'pending'

"""
Ensure Booking object stringifies
"""
def test_booking_stringifies():
    booking = Booking(1, 2, 3, '2026-01-20')

    assert str(booking) == "Booking(1, 2, 3, 2026-01-20, pending)"