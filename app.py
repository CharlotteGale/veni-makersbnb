from flask import Flask, request, render_template
from lib.database_connection import DatabaseConnection
from lib.listing_repository import ListingRepository

app = Flask(__name__)


connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.seed("seeds/makersbnb_veni.sql")

repository = ListingRepository(connection)


# == Your Routes Here ==

# # GET /index
# # Returns the homepage
# # Try it:
# #   ; open http://localhost:5001/index
# @app.route('/index', methods=['GET'])
# def get_index():
#     return render_template('index.html')

# # These lines start the server if you run this file directly
# # They also start the server configured to use the test database
# # if started in test mode.
# if __name__ == '__main__':
#     app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


@app.route("/")
def index():
    page = int(request.args.get("page", 1))
    per_page = 3

    # Get all listings from the database
    all_listings = repository.all()

    # Pagination logic
    start = (page - 1) * per_page
    end = start + per_page
    listings = all_listings[start:end]

    has_prev = page > 1
    has_next = end < len(all_listings)

    return render_template(
        "index.html",
        listings=listings,
        page=page,
        has_prev=has_prev,
        has_next=has_next
    )




if __name__ == "__main__":
    app.run(debug=True)