class User:
    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.password}, {self.name})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__