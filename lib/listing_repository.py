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
    
    def find(self, listing_id):
        rows = self._connection.execute(
            'SELECT * from listings WHERE id = %s',
            [listing_id])
        row = rows[0]
        return Listing(row['id'], row['user_id'], row['name'], row['description'],row['price_per_night'])

    def search_by_name(self, keyword):
        rows = self._connection.execute(
            'SELECT * from listings WHERE name ILIKE %s',
            [f'%{keyword}%'])
        return [
            Listing(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night'])
            for row in rows
        ]


