# http GET 'https://api.spotify.com/v1/playlists/45qu5W1B8DYYdoVhoJ7woX?market=CA' \
#  Authorization:'Bearer BQBoqY...QMkCrU'

from header import ACCESS_TOKEN

import requests
import json


playlist_url = "https://api.spotify.com/v1/playlists/2gjZAgEKtMU7TMRO1scpV0?market=CA"

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def fetch_data(url, headers):
    # endpoint https://api.spotify.com/v1/artists/{id}

    response = requests.get(url, headers=headers)
    return response.content


def get_playlist_information(data):
    data = json.loads(data)
    num_followers = data["followers"]["total"]

    owner = data["owner"]["display_name"]
    return owner


print(get_playlist_information(fetch_data(playlist_url, HEADERS)))
