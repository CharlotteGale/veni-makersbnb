import os
from lib.database_connection import get_flask_database_connection,  DatabaseConnection
from flask import Flask, request, render_template, redirect, session, flash
from lib.database_connection import DatabaseConnection
from lib.listing_repository import ListingRepository
from lib.booking_repository import BookingRepository
from lib.user_repository import UserRepository
from lib.user import User
from pathlib import Path
from lib.booking import Booking
from lib.booking_repository import BookingRepository


# ======================
# Create Flask app
# ======================
app = Flask(__name__)
app.secret_key = "dev-secret-key"

if os.environ.get("APP_ENV") == "PRODUCTION":
    conn = DatabaseConnection()
    conn.connect()
    conn.seed('seeds/makersbnb_veni.sql')
# ======================
# Database setup
# ======================
connection = DatabaseConnection(test_mode=False)
connection.connect()
# connection.seed(
#     Path(__file__).resolve().parent / "seeds" / "makersbnb_veni.sql"
# )



listing_repository = ListingRepository(connection)
booking_repository = BookingRepository(connection)
user_repository = UserRepository(connection)
booking_repository = BookingRepository(connection)


# ======================
# Routes
# ======================

@app.route("/")
def index():
    page = int(request.args.get("page", 1))
    per_page = 3

    all_listings = listing_repository.all()

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


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(
            None,
            request.form["email"],
            request.form["password"],
            request.form["name"]
        )

        user_repository.create(user)

        # Log user in after signup
        session["user_id"] = user.id
        session["user_name"] = user.name

        return redirect("/")

    return render_template("auth/signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = user_repository.authenticate(
            request.form["email"],
            request.form["password"]
        )

        if user:
            session["user_id"] = user.id
            session["user_name"] = user.name
            return redirect("/")

        flash("Invalid email or password")

    return render_template("auth/login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Placeholders for drop down menu
@app.route("/profile")
def profile():
    return "Profile page coming soon"

@app.route("/contact")
def contact():
    return "Contact page coming soon"


@app.route("/host/listings")
def host_listings():
    user_id = session.get("user_id")

    # /KS 22Jan2026/ If user not logged in, bounce to login. I know we may be asking the user to login before they can even see this option in the NAV bar but adding in for extra safety in case the link to this route is shared and bypasses any "UI walls".

    if user_id is None:
        flash("Please log in to view your listings.")
        return redirect("/login")

    # /KS 22Jan2026/ Pull ONLY this host's listings (secure server-side filter) - used filter search function from listing_repository.py
    listings = listing_repository.show_host_listings(user_id)

    return render_template(
        "host/listings.html", 
        host_listings=listings # /KS 22Jan2026/ host_listings is the listings variablenow plugged into to HTML template for host/listings
    )


@app.route("/guest/bookings")
def guest_bookings():
    user_id = session.get("user_id")

    # /KS 22Jan2026/ If user not logged in, bounce to login. I know we may be asking the user to login before they can even see this option in the NAV bar but adding in for extra safety in case the link to this route is shared and bypasses any "UI walls".

    if user_id is None:
        flash("Please log in to view your bookings.")
        return redirect("/login")
@app.route("/listings/<int:listing_id>")
def listing_booking(listing_id):
    listing = listing_repository.find(listing_id)

    if not listing:
        return "Listing not found", 404

    return render_template(
        "listings/booking.html",
        listing=listing
    )

@app.route("/listings/<int:listing_id>/book", methods=["POST"])
def create_booking(listing_id):
    if not session.get("user_id"):
        return redirect("/login")

    booking = Booking(
        None,
        listing_id,
        session["user_id"],
        request.form["date"],
        "pending"
    )

    booking_repository.create(booking)

    flash("Booking request submitted!")
    return redirect("/profile")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").lower()  # get search string, default empty

    all_listings = listing_repository.all()

    # Filter listings that contain the search in the name or description
    if query:
        filtered_listings = [
            listing for listing in all_listings
            if query in listing.name.lower() or query in listing.description.lower()
        ]
    else:
        filtered_listings = all_listings

    return render_template(
        "search_results.html",
        listings=filtered_listings,
        query=query
    )


    # /KS 22Jan2026/ Pull ONLY this guest's bookings- used filter search function from booking_repository.py
    bookings = booking_repository.show_guest_bookings(user_id)

    return render_template(
        "guest/bookings.html", 
        user_guest_bookings=bookings # /KS 22Jan2026/ user_guest_bookings is the bookings variable now plugged into to HTML template for guest/bookings
    )

# ======================
# Run server last
# ======================
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
"""if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))"""


if __name__ == '__main__':
    # We also run the server differently depending on the environment.
    # In production we don't want the fancy error messages — users won't know
    # what to do with them. So no `debug=True`
    if os.environ.get("APP_ENV") == "PRODUCTION":
        app.run(port=5002, host='0.0.0.0')
    else:
        app.run(debug=True, port=int(os.environ.get('PORT', 5002)))

