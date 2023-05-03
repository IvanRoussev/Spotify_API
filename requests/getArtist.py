from header import ACCESS_TOKEN

import requests


artist_url = "https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg"

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_artists(url, headers):
    # endpoint https://api.spotify.com/v1/artists/{id}

    response = requests.get(url, headers=headers)
    return response.content


print(get_artists(artist_url, HEADERS))
