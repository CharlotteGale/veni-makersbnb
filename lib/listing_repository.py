from lib.listing import Listing

class ListingRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM listings;'
        )
        
        return [
            Listing(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night'])
            for row in rows
        ]


    def create(self, listing):
        rows = self._connection.execute(
            'INSERT INTO listings (user_id, name, description, price_per_night) ' \
            'VALUES (%s, %s, %s, %s) ' \
            'RETURNING id;',
            [listing.user_id, listing.name, listing.description, listing.price_per_night]
        )
        row = rows[0]
        listing.id = row['id']
        return listing