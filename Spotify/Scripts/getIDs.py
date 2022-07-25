'''
Script that takes Billboard hot 100 song and artist
to search for Spotify ID for that song
'''



import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

cid = 'client id here'
secret = 'secret id here'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

year = 2000
# year = 2010

with open(f"../../Billboard/Data/{year}sSongs&Artists&FT.json", "r") as f:
  songs = json.load(f)


L = []
for song in songs:
  query = f"track:{song['song']} artist:{song['author']}"
  query = query.replace("'", "’")
  query = query.replace("(", "")
  query = query.replace(")", "")
  
  track_results = sp.search(
    q=f'{query}', 
    type='track', 
    market="US",
    limit=10,
  )
  data = track_results["tracks"]["items"]

  for id, item in enumerate(data):

    print(item["name"] + "vs\t" + song['song'])

    billboardAuthor = song["author"].strip().lower()
    spotifyArtist = item["artists"][0]["name"].strip().lower()
    billboardSong = song["song"].strip().lower()
    spotifySong = item["name"].strip().lower()
    
    
    if ((
          billboardAuthor == spotifyArtist 
          or billboardAuthor in spotifyArtist 
          or spotifyArtist in billboardAuthor)  
        and 
        ((
          spotifySong == billboardSong
          or billboardSong in spotifySong 
          or spotifySong in billboardSong))):
      L.append(item["id"])      
      print("match!!!!!!!")
      break
  print("------------------------------------------")

with open(f"{year}sIDs.json", "w") as f:
  json.dump(L, f)
