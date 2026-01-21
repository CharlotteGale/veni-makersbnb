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

"""
Ensure User object stringifies
"""
def test_user_stringifies():
    user = User(1, 'test@email.com', 'TestPassword!', 'Test User')

    assert str(user) == "User(1, test@email.com, TestPassword!, Test User)"

"""
Ensure 2 identical User objects are equal
"""
def test_identical_users_are_equal():
    user1 = User(1, 'test@email.com', 'TestPassword!', 'Test User')
    user2 = User(1, 'test@email.com', 'TestPassword!', 'Test User')

    assert user1 == user2