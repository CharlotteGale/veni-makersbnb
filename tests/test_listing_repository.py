from lib.listing_repository import ListingRepository
from lib.listing import Listing

"""
When we call ListingRepository#all
We get a list of Listing objects reflecting the seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = ListingRepository(db_connection)

    assert repo.all() == [
        Listing(1, 1, 'Cozy Canal Studio', 'Bright studio with canal views, fast WiFi, and a comfy queen bed — perfect for a weekend escape.', 95),
        Listing(2, 2, 'Shoreditch Loft Apartment', 'Trendy open-plan loft in the heart of Shoreditch, minutes from coffee spots, nightlife, and the Tube.', 160),
        Listing(3, 3, 'Countryside Barn Retreat', 'Peaceful converted barn with countryside walks, a wood burner, and beautiful sunset views.', 140),
        Listing(4, 2, 'Luxury City Penthouse', 'Modern penthouse with skyline views, floor-to-ceiling windows, balcony seating, and premium finishes.', 320),
        Listing(5, 4, 'Budget-Friendly Private Room', 'Simple private room in a shared flat with great transport links — clean, safe, and ideal for solo travellers.', 55),
        Listing(6, 1, 'Trendy Shoreditch Studio', 'Awesome space near coffee shops and bars, great for experiencing this part of london in all its hipster glory', 145)
    ]



"""
When we call ListingRepository#create
We create a new Listing object reflecting the seed data
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = ListingRepository(db_connection)

    new_listing = repo.create(Listing(None, 1, 'Test Name', 'Test Description', 15))

    assert new_listing == Listing(7, 1, 'Test Name', 'Test Description', 15)


"""
When we call ListingRepository#find
We get a single Listing object reflecting the seed data.
"""

def test_get_single_record(db_connection): 
    db_connection.seed("seeds/makersbnb_veni.sql")
    repo = ListingRepository(db_connection)
    listing = repo.find(2)
    assert listing == Listing(2, 2, 'Shoreditch Loft Apartment', 'Trendy open-plan loft in the heart of Shoreditch, minutes from coffee spots, nightlife, and the Tube.', 160)

"""
When we call ListingRepository#search_by_name
We get listings where the name partially matches the search keyword.
"""

def test_search_by_name_returns_matching_listings(db_connection):
        db_connection.seed("seeds/makersbnb_veni.sql")
        repo = ListingRepository(db_connection)

        search_results = repo.search_by_name('Shoreditch')

        assert search_results == [
                Listing(2, 2, 'Shoreditch Loft Apartment',
                'Trendy open-plan loft in the heart of Shoreditch, minutes from coffee spots, nightlife, and the Tube.',
                160),
                Listing(6, 1, 'Trendy Shoreditch Studio', 'Awesome space near coffee shops and bars, great for experiencing this part of london in all its hipster glory', 145)]

def test_search_by_name_returns_matching_listings_uppercase(db_connection):
        db_connection.seed("seeds/makersbnb_veni.sql")
        repo = ListingRepository(db_connection)

        search_results = repo.search_by_name('SHOREDITCH')

        assert search_results == [
                Listing(2, 2, 'Shoreditch Loft Apartment',
                'Trendy open-plan loft in the heart of Shoreditch, minutes from coffee spots, nightlife, and the Tube.',
                160),
                Listing(6, 1, 'Trendy Shoreditch Studio', 'Awesome space near coffee shops and bars, great for experiencing this part of london in all its hipster glory', 145)]

"""
When we call ListingRepository#delete
The listing record is deleted from the database.
"""

# def test_delete_listing():
#         db_connection.seed("seeds/makersbnb_veni.sql")
#         repo = ListingRepository(db_connection)
