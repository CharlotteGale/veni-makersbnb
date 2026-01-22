class Booking:
    def __init__(self, id, listing_id, guest_id, date, status='pending', listing_name=None, listing_description=None, price_per_night=None):
        self.id = id
        self.listing_id = listing_id
        self.guest_id = guest_id
        self.date = date
        self.status = status
        self.listing_name = listing_name
        self.listing_description = listing_description
        self.price_per_night = price_per_night

    def __repr__(self):
        return f"Booking({self.id}, {self.listing_id}, {self.guest_id}, {self.date!r}, {self.status})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__gi