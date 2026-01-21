

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        rows = self._connection.execute(
            'INSERT INTO users (email, password, name) ' \
            'VALUES (%s, %s, %s) ' \
            'RETURNING id;',
            [user.email, user.password, user.name]
        )
        row = rows[0]
        user.id = row['id']
        return user