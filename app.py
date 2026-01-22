import os
from flask import Flask, request, render_template, redirect, session, flash

from lib.database_connection import DatabaseConnection
from lib.listing_repository import ListingRepository
from lib.user_repository import UserRepository
from lib.user import User
from pathlib import Path
from lib.listing import Listing


# ======================
# Create Flask app
# ======================
app = Flask(__name__)
app.secret_key = "dev-secret-key"

# ======================
# Database setup
# ======================
connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.seed(
    Path(__file__).resolve().parent / "seeds" / "makersbnb_veni.sql"
)


listing_repository = ListingRepository(connection)
user_repository = UserRepository(connection)

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

from flask import request, redirect, render_template, session, flash

@app.route("/host/add_listing", methods=["GET", "POST"])
def add_listing():
    user_id = session.get("user_id")

    if user_id is None:
        flash("Please log in to add a listing.")
        return redirect("/login")

    if request.method == "POST":
        listing = Listing(
            id=None,
            name=request.form["name"],
            description=request.form["description"],
            price_per_night=request.form["price_per_night"],
            user_id=user_id,
        )

        listing_repository.create(listing)

        flash("Listing added successfully!")
        return redirect("/host/listings")

    return render_template("host/add_listing.html")







# ======================
# Run server (LAST)
# ======================
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
