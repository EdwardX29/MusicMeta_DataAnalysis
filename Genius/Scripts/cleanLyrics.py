'''
Since Genius website often returns advertisements for other songs with features
this file aims to remove all of those unwanted advertisements from lyrics
'''

year = 2000
# year = 2010

with open(f"../Data/{year}sLyrics.txt", "r") as f:
    contents = f.readlines()

for line in contents:
    if line.count("ft.") > 5: pass # remove genius advertisement text from lyrics 
    else:
        with open(f"cleaned{year}sLyrics.txt", "a") as c:
            c.write(line)
