from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (listing_id, guest_id, date, status) ' \
            'VALUES (%s, %s, %s, %s) ' \
            'RETURNING id;',
            [booking.listing_id, booking.guest_id, booking.date, booking.status]
        )
        row = rows[0]
        booking.id = row['id']
        return booking
    
    def show_guest_bookings(self, guest_id):
        rows = self._connection.execute(
        'SELECT * FROM bookings WHERE guest_id = %s ORDER BY id;',
        [guest_id]
        )
        return [
        Booking(row['id'], row['listing_id'], row['guest_id'], row['date'], row['status'])
        for row in rows
        ]

