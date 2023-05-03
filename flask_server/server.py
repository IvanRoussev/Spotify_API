from flask import Flask
from request_data import getArtist

app = Flask(__name__)


# Artist API route
@app.route("/artist")
def artist():
    # main() should return the output below
    # {'name': 'Pitbull', 'followers': 9965353, 'popularity_rating': 83, 'list_genres': ['dance pop', 'miami hip hop', 'pop']}
    return getArtist.main()


if __name__ == "__main__":
    app.run(debug=True)
