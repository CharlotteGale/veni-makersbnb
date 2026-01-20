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
