import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

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

class FakeListing:
    def __init__(self, name, description, price_per_night):
        self.name = name
        self.description = description
        self.price_per_night = price_per_night


@app.route("/")
def index():
    fake_listings = [
        {
            "name": "Cozy Flat",
            "description": "Close to city centre",
            "price_per_night": 95,
            "image_filename": "flat1.jpg"
        },
        {
            "name": "Beach House",
            "description": "Sea views",
            "price_per_night": 150,
            "image_filename": None
        },
                {
            "name": "Cozy Flat",
            "description": "Close to city centre",
            "price_per_night": 95,
            "image_filename": "flat1.jpg"
        },
        {
            "name": "Beach House",
            "description": "Sea views",
            "price_per_night": 150,
            "image_filename": None
        },
    ]

    page = int(request.args.get("page", 1))
    per_page = 3

    start = (page - 1) * per_page
    end = start + per_page

    listings = fake_listings[start:end]

    has_prev = page > 1
    has_next = end < len(fake_listings)

    return render_template(
        "index.html",
        listings=listings,
        page=page,
        has_prev=has_prev,
        has_next=has_next
    )



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)