import bcrypt

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        hashed_password = bcrypt.hashpw(
            user.password.encode('utf-8'),
            bcrypt.gensalt()
        )


        rows = self._connection.execute(
            'INSERT INTO users (email, password, name) ' \
            'VALUES (%s, %s, %s) ' \
            'RETURNING id;',
            [user.email, hashed_password.decode('utf-8'), user.name]
        )
        row = rows[0]
        user.id = row['id']
        return user