from lib.listing import Listing

'''
We can ensure the listing object constructs with an id, user_id, name, description and price per night. 

'''
def test_listing_constructs():
    listing = Listing(1, 1, "test name", "test description", 20)
    assert listing.id == 1
    assert listing.user_id == 1
    assert listing.name == "test name"
    assert listing.description == "test description"
    assert listing.price_per_night == 20

'''
We want to ensure the object stringifies

'''
def test_listing_stringifies():
    listing = Listing(1, 1, "test name", "test description", 20)
    assert str(listing) == "Listing(1, 1, test name, test description, 20)"
