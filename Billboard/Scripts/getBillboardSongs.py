'''
Used to collect all the songs from 2000s and 2010s
from Billboard's Weekly Hot 100 Lists 
'''

import billboard
import datetime
import json

# Dates for 2010s
decade = 2000
cutOffDate = datetime.date(2010, 1,1)
currentDate = datetime.date(2020,1,1)

# Dates for 2000s
# decade = 2010
# cutOffDate = datetime.date(2000, 1,1)
# currentDate = datetime.date(2010,1,1)

chart = billboard.ChartData("hot-100", date=currentDate)

songs = []

def getSongs():
    for song in chart:
        songs.append(song.title + " by " + song.artist)

while currentDate > cutOffDate:
    getSongs()
    prevDate = currentDate - datetime.timedelta(days=7)

    chart = billboard.ChartData("hot-100", prevDate)
    currentDate = prevDate
    

with open(f"BillboardWithDuplicates{decade}.json", "w") as file:
    json.dump(songs,file,indent=2)

with open(f"BillboardNoDuplicates{decade}.json", "w") as file:
    json.dump(list(set(songs)), file, indent = 2)
