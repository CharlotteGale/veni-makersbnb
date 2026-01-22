class Booking:
    def __init__(self, id, listing_id, guest_id, date, status='pending'):
        self.id = id
        self.listing_id = listing_id
        self.guest_id = guest_id
        self.date = date
        self.status = status

    def __repr__(self):
        return f"Booking({self.id}, {self.listing_id}, {self.guest_id}, {self.date!r}, {self.status})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__