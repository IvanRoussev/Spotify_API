## Client ID

### 4069f434f74944959fccee1c29d8782f

## Client Secret

### fdd370d87ed2480b9f43d6afde8a6c85

## Command To get Token

### curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=4069f434f74944959fccee1c29d8782f&client_secret=fdd370d87ed2480b9f43d6afde8a6c85"

## Token

## {"access_token":"BQD6bmuQX7R6zQcCHtDRYT7S9hczmBz9T4kM2thcIcOwRCadrEF7Lr-67TqLVZq2U7m0kAPDIYocCipPd9ZoNfDntDe5fbkCXvtGlVTCKkw5z5Gxt-Tx","token_type":"Bearer","expires_in":3600}

## To Get Access Token

### You need Client Id and Client Secret

- To find Client Id and Secret Vists
  https://developer.spotify.com/dashboard/

## Client ID

### 4069f434f74944959fccee1c29d8782f

## Client Secret

### fdd370d87ed2480b9f43d6afde8a6c85

## Command To get Token

### curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=4069f434f74944959fccee1c29d8782f&client_secret=fdd370d87ed2480b9f43d6afde8a6c85"

## Token

## {"access_token":"BQD6bmuQX7R6zQcCHtDRYT7S9hczmBz9T4kM2thcIcOwRCadrEF7Lr-67TqLVZq2U7m0kAPDIYocCipPd9ZoNfDntDe5fbkCXvtGlVTCKkw5z5Gxt-Tx","token_type":"Bearer","expires_in":3600}

## To Get Access Token

### You need Client Id and Client Secret

- To find Client Id and Secret Vists
  https://developer.spotify.com/dashboard/

<picture>
  <img alt="client_id" src="./images/client_id.png">
</picture>

<picture>
  <img alt="client_secret" src="./images/client_secret.png">
</picture>

### 1. Make a curl request using this command

**Replace client_id with your client_id and your client secret with secret**

curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id="<client_id>"&client_secret="<client_secret>""
