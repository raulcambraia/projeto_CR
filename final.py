import os
import base64
from requests import post, get
import json

token = "BQA4QAa7wcxvc69CuW4iU5meGnqkgRl6NTqNrhGBzQxOzj48E_eZJH68gK2cfR5sCQihLmAINlsH1chFjFwJ3fHEzN6NAOxJhzRJ9vQ9l9mLspNC6I2CDmmQ9r8ExHJ2jyPll8n5TbqD9S7y_42YiWcscy6ZFcVMAauAbUfhwBnq-Oh1bv-oeAPXTVU5pxqja1XoM-p0KMAnXw"
artist_id = str(input("digite o id do artista"))

 """
 o código final, estava sendo muito trabalhoso e fugindo do escopo do projeto. Sendo assim, optamos por seguir com o básico, apenas a função de retornar os artistas relacionados e um print para lista-los juntamente com o ID, de forma que o processo se tornou manual
 """

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
              
def get_artist_related(token, artist_id):
  url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
  headers = get_auth_header(token)
  result = get(url, headers=headers)
  json_result = json.loads(result.content)["artists"]
  return json_result
related_artists = get_artist_related(token, artist_id)

for artists in related_artists:
 print(f"{artists['name']}")
for artists in related_artists:
  print(f"{artists['id']}") 

