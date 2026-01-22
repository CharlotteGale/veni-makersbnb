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
        'SELECT * FROM booking_detials WHERE guest_id = %s ORDER BY id;',
        [guest_id]
        )
        return [
        Booking(row['id'], row['listing_id'], row['guest_id'], row['date'], row['status'], row['listing_name'], row['listing_description'],row['price_per_night'])
        for row in rows
        ]

    def confirm_booking(self, booking_id):
        self._connection.execute(
            'UPDATE bookings SET status = %s WHERE id = %s;',
            ['confirmed', booking_id]
        )

    def reject_booking(self, booking_id):
        self._connection.execute(
            'UPDATE bookings SET status = %s WHERE id = %s;',
            ['rejected', booking_id]
        )
