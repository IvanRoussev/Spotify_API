from .header import ACCESS_TOKEN

import requests
import json


artist_url = "https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg"

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def fetch_data(url, headers):
    # endpoint https://api.spotify.com/v1/artists/{id}

    response = requests.get(url, headers=headers)
    return response.content


def get_artist_information(data):
    data = json.loads(data)
    # print(data)
    name = data["name"]
    followers = data["followers"]["total"]
    popularity_rating = data["popularity"]
    list_genres = data["genres"]
    # print(name)
    # print(followers)
    # print(popularity_rating)
    # print(list_genres)
    artist_dict = {
        "name": name,
        "followers": followers,
        "popularity_rating": popularity_rating,
        "list_genres": list_genres,
    }
    return artist_dict


def main():
    return get_artist_information(fetch_data(artist_url, HEADERS))


# print(main())
