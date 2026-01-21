from lib.user_repository import UserRepository
from lib.user import User

"""
When I call UserRepository#create
I add a new User object to the seed data 
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = UserRepository(db_connection)

    new_user = repo.create(User(None, 'test@email.com', 'TestPassword!', 'Test User'))

    assert new_user == User(1, 'test@email.com', 'TestPassword!', 'Test User')