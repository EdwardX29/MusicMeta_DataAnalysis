'''
Using spotify IDs, use Spotify's audio features endpoint
to get musical aspect data on each song
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
  ids = json.load(f)

L = []

for id in ids:
  L.append(sp.audio_features(id))

with open(f"{year}sMusicalAspects.json", "w") as f:
  json.dump(L, f, indent=4)
