class Listing:
    def __init__(self, id, user_id, name, description, price_per_night):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night


    def __repr__(self):
        return f"Listing({self.id}, {self.user_id}, {self.name}, {self.description}, {self.price_per_night})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__