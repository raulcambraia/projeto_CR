from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_artist_related(token, artist_id):
 url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
 headers = get_auth_header(token)
 result = get(url, headers=headers)
 json_result = json.loads(result.content)["artists"]
 return json_result

token = get_token()
artist_id = "0TnOYISbd1XYRBk9myaseg"
related_artists = get_artist_related(token, artist_id)


for artists in (related_artists):
   print(f"{artists['name']}")

"""
primeiro teste: acesso ao token de forma automatizada e apenas a função de printar os artistas a fim de teste
"""
