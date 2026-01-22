from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (listing_id, guest_id, date, status) '\
            'VALUES (%s, %s, %s, %s) '\
            'RETURNING id;',
            [booking.listing_id, booking.guest_id, booking.date, booking.status]
        )
        booking.id = rows[0]['id']
        return booking

    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings;')
        return [
            Booking(row['id'], row['listing_id'], row['guest_id'], str(row['date']), row['status'])
            for row in rows
        ]
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

    def check_dates(self, listing_id, date):
        rows = self._connection.execute(
            'SELECT status FROM bookings ' \
            'WHERE listing_id = %s ' \
            'AND status = %s ' \
            'AND date = %s;',
            [listing_id, 'confirmed', date]
        )

        return len(rows) == 0
    
    def get_pending_bookings_for_host(self, user_id):
        rows = self._connection.execute(
            'SELECT b.* FROM bookings b ' \
            'JOIN listings l ON b.listing_id = l.id ' \
            'WHERE l.user_id = %s AND b.status = %s ' \
            'ORDER BY b.date, b.id;',
            [user_id, 'pending']
        )
        return [
            Booking(row['id'], row['listing_id'], row['guest_id'], str(row['date']), row['status'])
            for row in rows
        ]

        
