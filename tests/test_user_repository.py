from lib.user_repository import UserRepository


"""
When I call UserRepository#create
I add a new User object to the seed data 
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = UserRepository(db_connection)

    new_user = repo.create(User(None, 'test@email.com', 'TestPassword!', 'Test User'))

    assert new_user.id == 1
    assert new_user.email == 'test@email.com'
    assert new_user.password == 'TestPassword!'
    assert new_user.name == 'Test User'