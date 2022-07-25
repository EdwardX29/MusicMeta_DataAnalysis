'''
Script that gets the genres of all songs using song IDs
'''

import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'client id here'
secret = 'secret id here'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

year = 2000
# year = 2010

with open(f"../Data/{year}sIDs.json", "r") as f:
  contents = json.load(f)

genreList = []
genreMap = {}

for id in contents:
  result = sp.track(id)
  result = result["artists"][0]["id"]
  
  genres = sp.artist(result)["genres"]
  genreList.append(genres)

  for genre in genres:
    if genre not in genreMap.keys():
      genreMap[genre] = 1
    else:
      genreMap[genre] = genreMap[genre] + 1
  
with open(f"../Data/{year}genreList.json", "w") as f:
  json.dump(genreList, f, indent=4)

with open(f"../Data/{year}genreMap.json", "w") as f:
  json.dump(genreMap, f, indent=4)
