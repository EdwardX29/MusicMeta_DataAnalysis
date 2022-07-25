'''
File used to modify the original song lists from Billboard
The original song lists stored songs and artists as strings on the same line

This file splits songs and artists into dictionaries 
with values song & author & feature artists
'''

import json

decade = 2000
# decade = 2010

with open(f"BillboardNoDuplicates{decade}.json", "r") as f:
    fileContent = json.load(f)

dictList = []
for item in fileContent:
    stringLeft = item.rsplit(" by ", 1)
    author = stringLeft[-1].strip()
    song = stringLeft[0].strip()

    if "Featuring" in author:
        splitArr = author.rsplit("Featuring")
        author = splitArr[0].strip()
        feature = splitArr[-1].strip()
    else:
        feature = ""

    dictList.append(
        {
        'author': author,
        'song' : song,
        'featuring': feature
        }
    )

with open(f"{decade}sSongs&Artists&FT.json" , "w")  as f:
    json.dump(dictList, f, indent=2)