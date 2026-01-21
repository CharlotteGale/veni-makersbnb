from lib.user import User

"""
Ensure User object constructs
"""
def test_user_constructs():
    user = User(1, 'test@email.com', 'TestPassword!', 'Test User')

    assert user.id == 1
    assert user.email == 'test@email.com'
    assert user.password == 'TestPassword!'
    assert user.name == 'Test User'