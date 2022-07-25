'''
File to collect the lyrics for songs using Genius API 
& song/artist data collected from Billboard
'''


from lyricsgenius import Genius
import os
import re 
import json

token = "your genius token here"
genius = Genius(token)

year = 2000
# year = 2010

with open(f"../../Billboard/Data/{year}sSongs&Artists&FT.json", "r") as f:
  contents = json.load(f)

i = 0

while i < len(contents):
  try:
    
    song = genius.search_song(f"{contents[i]['song']}", f"{contents[i]['author']}")
    if song is not None:
      lyrics = song.lyrics
      lyrics = lyrics.split("Lyrics", 1)[-1]
      lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
      lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
      lyrics = " ".join(lyrics.split("\n"))
      lyrics = lyrics.split(" ")
      lyrics[-1] = re.sub(r"Embed", '', re.sub(r'[0-9]+', '', lyrics[-1]))
      lyrics = " ".join(lyrics)
      
      with open(f"../Data/{year}sLyrics.txt", "a") as f:
        f.write(str(lyrics) +  '\n')
        
    i+=1
  except:
    print("repeating")
    pass

print("done")