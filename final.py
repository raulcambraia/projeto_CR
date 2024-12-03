from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import pandas as pd
#import numpy as np

#from main import get_auth_header

token = "BQA4QAa7wcxvc69CuW4iU5meGnqkgRl6NTqNrhGBzQxOzj48E_eZJH68gK2cfR5sCQihLmAINlsH1chFjFwJ3fHEzN6NAOxJhzRJ9vQ9l9mLspNC6I2CDmmQ9r8ExHJ2jyPll8n5TbqD9S7y_42YiWcscy6ZFcVMAauAbUfhwBnq-Oh1bv-oeAPXTVU5pxqja1XoM-p0KMAnXw"
artist_id = str(input("bbbbbb"))
#i = k = 0

 

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
              
def get_artist_related(token, artist_id):
  url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
  headers = get_auth_header(token)
  result = get(url, headers=headers)
  json_result = json.loads(result.content)["artists"]
  return json_result
related_artists = get_artist_related(token, artist_id)
"""
def search_for_artist(token, artist_name):
  url = f"https://api.spotify.com/v1/search"
  headers = get_auth_header(token)
  result = get(url, headers=headers)
  json_result = json.loads(result.content)["artists"]["items"]
  return json_result
artist_id = search_for_artist(token, "Taylor Swift")

for artist in artist_id:
  print(f"{artist['id']}")  
"""
for artists in related_artists:
 print(f"{artists['name']}")
for artists in related_artists:
  print(f"{artists['id']}") 



"""

for i in list_of_id:
  artist_id = list_of_id[i]
  if i == 100:
    break
  else:
    for artists in (related_artists):
     dados = {
       'artista1': (f"{artists['name']}")
       'artista2'
       } 
     list_of_id.append(f"{artists['id']}")
      



for artists in (related_artists):
 list_of_artists.append(f"{artists['name']}")
 list_of_id.append(f"{artists['id']}")

def create_list(related_artists, artist_id):
 list_of_id = [artist_id]
 #while k < 5:
 for j in len(list_of_id):
   artist_id = list_of_id[j]
   for artists in (related_artists):
    list_of_artists.append(f"{artists['name']}")
    list_of_id.append(f"{artists['id']}")
    i = i + 1
    if i == 5:
     print(list_of_artists)
     list_of_artists.clear()
     k = k + 1 
    break
  #print(list_of_id)   
"""  