from nltk.corpus import stopwords

year = 2000
# year = 2010


with open("clean2010.txt", "r") as f:
    lines = f.readlines()

wordList = []

for line in lines:

    words = line.split(" ")
    for word in words:
        if word not in stopwords.words('english'):
            wordList.append(word.strip().lower())

import json

with open("wordList2010.txt", "w") as f:
    json.dump(wordList, f, indent=4)

with open("wordSet2010.txt", "w") as f:
    json.dump(list(set(wordList)), f, indent=4)  
    