from lib.user_repository import UserRepository
from lib.user import User

"""
When I call UserRepository#create
I add a new User object to the seed data 
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = UserRepository(db_connection)

    new_user = repo.create(User(1,'test@email.com', 'TestPassword!', 'Test User'))

    assert new_user.id is not None
    assert new_user.email == 'test@email.com'
    assert new_user.name == 'Test User'

"""
When I call UserRepository#create
I know that the password has been stored in the database
"""
def test_password_is_stored_in_database(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = UserRepository(db_connection)

    new_user = repo.create(User(1,'test@email.com', 'TestPassword!', 'Test User'))

    result = db_connection.execute(
        'SELECT password FROM users ' \
        'WHERE id = %s;',
        [new_user.id]
    )

    assert result[0]['password'] == 'TestPassword!'

"""
When I call UserRepository#create
I want to ensure that the password is stored securely
"""
def test_password_is_hashed_not_plain_text(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = UserRepository(db_connection)

    new_user = repo.create(User(1,'test@email.com', 'TestPassword!', 'Test User'))

    result = db_connection.execute(
        'SELECT password FROM users ' \
        'WHERE id = %s;',
        [new_user.id]
    )
    stored_password = result[0]['password']

    assert stored_password != 'TestPassword!'
    assert stored_password.startswith('$2b$')