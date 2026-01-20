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
    listings = [
        # FakeListing(
        #     "Cosy Studio Flat",
        #     "A quiet studio close to the city centre.",
        #     75
        # ),
        # FakeListing(
        #     "Modern Loft",
        #     "Open-plan loft with lots of natural light.",
        #     120
        # ),
        # FakeListing(
        #     "Country Cottage",
        #     "Peaceful countryside retreat with beautiful views.",
        #     60
        # ),
    ]

    return render_template("index.html", listings=listings)


if __name__ == "__main__":
    app.run(debug=True)