import requests


ACCESS_TOKEN = "BQD6bmuQX7R6zQcCHtDRYT7S9hczmBz9T4kM2thcIcOwRCadrEF7Lr-67TqLVZq2U7m0kAPDIYocCipPd9ZoNfDntDe5fbkCXvtGlVTCKkw5z5Gxt-Tx"

artist_url = "https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_artists(url, headers):
    # endpoint https://api.spotify.com/v1/artists/{id}

    response = requests.get(url, headers=headers)
    return response.content


print(get_artists(artist_url, headers))
