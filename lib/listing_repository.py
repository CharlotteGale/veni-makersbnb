from lib.listing import Listing

class ListingRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM listings ORDER BY id;'
        )
        
        return [
            Listing(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night'], row['image_filename'])
            for row in rows
        ]


    def create(self, listing):
        rows = self._connection.execute(
            'INSERT INTO listings (user_id, name, description, price_per_night, image_filename) ' \
            'VALUES (%s, %s, %s, %s, %s) ' \
            'RETURNING id;',
            [listing.user_id, listing.name, listing.description, listing.price_per_night,listing.image_filename]
        )
        row = rows[0]
        listing.id = row['id']
        return listing
    
    def find(self, listing_id):
        rows = self._connection.execute(
            'SELECT * from listings WHERE id = %s ORDER BY id;',
            [listing_id])
        row = rows[0]
        return Listing(row['id'], row['user_id'], row['name'], row['description'],row['price_per_night'], row['image_filename'])

    def search_by_name(self, keyword):
        rows = self._connection.execute(
            'SELECT * from listings WHERE name ILIKE %s ORDER BY id;',
            [f'%{keyword}%'])
        return [
            Listing(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night'], row['image_filename'])
            for row in rows
        ]


    def show_host_listings(self, user_id):
        rows = self._connection.execute(
        'SELECT * FROM listings WHERE user_id = %s ORDER BY id;',
        [user_id]
        )
        return [
        Listing(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night'], row['image_filename'])
        for row in rows
        ]

