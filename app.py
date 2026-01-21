import os
from flask import Flask, request, render_template, redirect, session, flash

from lib.database_connection import DatabaseConnection
from lib.listing_repository import ListingRepository
from lib.user_repository import UserRepository
from lib.user import User

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
connection.seed("seeds/makersbnb_veni.sql")

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



# ======================
# Run server (LAST)
# ======================
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
