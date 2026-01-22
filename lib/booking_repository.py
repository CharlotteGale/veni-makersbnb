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
    
    def confirm_booking(self, booking_id):
        self._connection.execute(
            'UPDATE bookings SET status = %s WHERE id = %s;',
            ['confirmed', booking_id]
        )