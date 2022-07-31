'''
Used to collect all the songs from 2000s and 2010s
from Billboard's Weekly Hot 100 Lists 
'''

import billboard
import datetime
import json


decade = 2010
cutOffDate = datetime.date(2010, 1,1)
currentDate = datetime.date(2020,1,1)
chart = billboard.ChartData("hot-100", date=currentDate)

songs = []

while currentDate > cutOffDate:
    chart = billboard.ChartData("hot-100", enddate)
    for song in chart:
        songs.append(song.title + " - " + song.artist)
    enddate = enddate - datetime.timedelta(days = 7)

with open(f"BillboardWithDuplicates{decade}.json", "w") as file:
    json.dump(songs,file,indent=2)

with open(f"BillboardNoDuplicates{decade}.json", "w") as file:
    json.dump(list(set(songs)), file, indent = 2)
