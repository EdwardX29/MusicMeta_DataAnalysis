# Musical Metamorphasis: A Study of the Evolution of Popular Music (2000s & 2010s)
### A final [Ulysses Research](https://sites.google.com/mcpsmd.net/ulysses/home) project by Edward Xiao (NWHS '22)   
---

<img src="https://user-images.githubusercontent.com/69602889/184269248-dbe18bf2-5901-4714-80ed-309f0200090b.jpg" alt="drawing" width="600"/>

> Ed at his table at the Ulysses Fair

---
## Project Presentation video
https://user-images.githubusercontent.com/69602889/184217957-7ffea64e-420a-445e-a5ec-2043ec1b3e4b.mp4

---
## Table of Contents
1. [Abstract](#i-abstract)
2. [Questions](#ii-questions)
3. [Background Research](#iii-background-research)
4. [Data Collection](#iv-data-collection)
5. [Analysis & Results](#v-analysis--results)
6. [Discussion](#vi-discussion--future-improvements)
   

---
## I. Abstract
Music is an integral part of culture around the world. From the beginning of human history to the present day, music has played an important role in the development of culture and expression. Although its ubiquity and pervasive influence is difficult to deny, its ability to adapt in different time periods and geographic locations is an aspect that truly makes it unique. In the digital age, music has become an increasingly important part of pop culture as the internet (with its wide range of music streaming platforms) has made it easy to access music. At the same time, music creation software has allowed artists to create songs faster and at less cost than previous eras. Because of this newfound accessibility to music streaming and music creation software, there has been an uptick in music production and consumption. These revolutions have facilitated an environment where evolution and change in musical elements have occurred. Even between brief periods of time like the twenty years between 2000 and 2020--which pale in comparison to the length of musical history in totality--changes in popular music have inspired debates over what musical elements have created the greatest impact in distinguishing pop music eras.  

[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)
   
   

---
## II. Questions
In order to better investigate how music has changed from the 2000s to the 2010s, I have divided my broad primary research question into the following sub-questions:
* How has musical valence ([the measure of happiness](https://web.stanford.edu/~elenatuz/courses/stats32-aut2021/Spotify_analysis.html#:~:text=valence%20%3A%20A%20measure%20from%200.0,sad%2C%20depressed%2C%20angry)) changed between the eras 2000-2010 and 2010-2020?
* In what ways has the diversity of lyrical content in pop music evolved in the last two decades?
* Which elements of pop music remained the same throughout the years?
* How has the role of collaboration changed between these two decades?
   
[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s) 
     
---
## III. Background Research
[Full literature review](https://github.com/EdwardX29/MusicMeta_DataAnalysis/files/9312450/lit-review.docx)        
[Working Bibliography](https://github.com/EdwardX29/MusicMeta_DataAnalysis/files/9313073/WorkingBib.docx)


### **Interiano, Myra, et al. "Musical Trends and Predictability of Success in Contemporary Songs in and out of the Top Charts."**

* Researchers found that successful pop songs were happier, more danceable, and had brighter timbres than their unsuccessful counterparts. 
* At the same time, researchers also discovered that popular songs have changed in their musical characteristics particularly:
    1. Becoming less aggressive
    2. Utilizing more female vocals
    3. Using more negative, anti-social, and violent lyrics

### **Schellenberg, E. Glenn, and Christian Von Scheve. "Emotional Cues in American Popular Music: Five Decades of the Top 40."**
* Tempo has been on the rise, increasing roughly 1.4 seconds per year on average between years 1965 and 2009
* The proportion of male artists is declining (from ~80% of  charting pop songs in the late 20th century to ~60% in the 21st century)
* Sad-sounding songs have become more prevalent alongside "ambiguous" songs–-songs that are not obviously happy or sad

### **Brand, Charlotte O., et al. "Cultural Evolution of Emotional Expression in 50 Years of Song Lyrics."**
* A sentiment analysis of ~200,000 songs from 1965 to 2010 revealed that lyrics have become less positive
* Researchers analyzed 3 sources of bias that could have caused this negative shift:
    1. Success bias: artists imitating successful older songs
    2. Prestige bias: artists imitating successful past artists
    3. Content bias: general audience preference towards negative lyrics
* After analyzing data with multiple statistical models--Bayesian, aggregated binomial, and multilevel-- researchers concluded that content bias was the greatest predictor for increasingly negative lyrics, as opposed to prestige bias or success bias
* Researchers attribute the increase of negative lyrics to random drift (natural variation) or music-specific negativity bias 

### **Varnum, Michael E. W., et al. "Why are Song Lyrics Becoming Simpler? A Time Series Analysis of Lyrical Complexity in Six Decades of American Popular Music."**
* Song lyrics have become simpler over time as shown by an analysis of lyrical compressibility of pop music from 1958 to 2016
* Researchers were able to find that simpler lyrics were strongly associated with the presence of newer musical production
* Researchers believe that simpler song lyrics could be attributed to the following factors:   
    1. Cultural influences
    2. Complex lyrics could obstruct the enjoyability of the song to certain listeners, deterring them from listening again
    3. The increasing quantity of songs released each year by virtue of the internet or other distribution services
* The researchers conjecture that artists who utilize simpler lyrics could attract new listeners while stifling competition with memorable song snippets 

### **Mauch, Matthias, et al. "The Evolution of Popular Music: USA 1960–2010."**

* Some musical features like "dominant 7th chords", "male voice, vocal" and "piano, orchestra, harmonic" have seen very little change in frequency between the 1960s and 2000s
*  Other musical motifs like "minor-seventh chords" and "energetic, speech, bright" have seen gradual growth in frequency in alignment with the rise of particular genres in popular music
* The rise and fall of genres has also potentially caused fluctuations in musical diversity--the number of unique songs and styles
* Many "in-style" musical elements see notable growth before stabilizing at an equilibrium level
    * This suggests that momentary diversity (or lack thereof) is correlated strongly with genre-specific growth or decline, not a permanent trend of music

[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)
   

---
## IV. Data Collection

### **Overview**

Beginning with my data collection process, I had to set a definition of what a popular song is. After all, just like other music history researchers have noted, there could be a dozen metrics that constitute popularity of a song (including but not limited to a song’s streams, internet searches, and social media buzz). British researchers, Interiano et al, decided to rely on Top 100 Singles Chart by the Official Charts Company in the UK, a list that has legitimacy in the public eye. 

I decided that my definition of a popular song would be similar to that of other music researchers: songs that have a high ranking in popularity on a legitimate ranking list. As a result I chose to use the Billboard Top 100 List, a weekly ranking of the 100 most popular songs in the United States, as the source of my data.



### **Billboard Data Collection**

For my original research, I began by collecting the most popular songs from the years 2000 to 2020. For this task, I utilized the Billboard Top 100’s weekly song rankings for each week from 2000 to 2020. To accomplish this, I used [billboard.py](https://github.com/guoguo12/billboard-charts) to scrape all of the songs between the two decades 2000-2010 and 2010-2020. 

![image](https://user-images.githubusercontent.com/69602889/184446690-eb51dacc-5f88-455c-9a0a-ed6d6c08e065.png)   
> [Script](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Billboard/Scripts/getBillboardSongs.py) collecting all Billboard songs for 2000s & 2010s   

I saved all of the songs into json files and removed any repeating songs. In order to collect data on the songs, I had to ensure that I could write specific API queries. Thus, I organized each song into a list of JSON dictionaries where each song is a dictionary with keys representing song name, artist, and feature artist. 

![image](https://user-images.githubusercontent.com/69602889/184446437-e4a7f81c-b754-4bd1-9fc4-70a90be204d3.png)    
> [Script](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Billboard/Scripts/getArtistsFeatures.py) isolating song name, artist, and features   
    
![image](https://user-images.githubusercontent.com/69602889/184447244-c342ceb6-461d-4be7-92e9-680cbd33d925.png)
> [Result](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Billboard/Data/2000sSongs%26Artists%26FT.json) of data processing   


Next, I moved on to leveraging open source REST APIs, Spotify API (for musical insights) and Genius API (for lyrics), with my organized list of popular songs.  

The final organized data can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Billboard/Data)       
The data collection and data preprocessing scripts can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Billboard/Data)

### **Spotify Data Collection**

In order to answer the sub-questions "which elements of pop music remained the same throughout the years" and "How has musical valence changed between the eras 2000-2010 and 2010-2020?", I enlisted the help of Spotify API's [Audio Features Endpoint](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features) and [Spotipy](https://spotipy.readthedocs.io/en/master/). This endpoint returns granular data about the audio features of a Spotify track. These audio features include valence, danceability, duration, and liveness among others.

In order to call the endpoint, however, one first needs to find Spotify's "track id" of a song. Using the song information collected from Billboard, one can use Spotify's [Search Endpoint](https://developer.spotify.com/documentation/web-api/reference/#/operations/search) to find track ids.      
![image](https://user-images.githubusercontent.com/69602889/184460821-11052c46-17a7-44dc-b210-d0312998d00c.png)     
> [Script](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Spotify/Scripts/getIDs.py) that uses Billboard data to search for Spotify track ID   

![image](https://user-images.githubusercontent.com/69602889/184461068-c1a1060d-8425-4239-826e-6be686a22e68.png)
> Track IDs for some 2000s songs

After collecting track IDs for as many songs as possible (some songs inevitably slip through the cracks due to the imperfect nature of Spotify's search queries), I collected the audio features data for each song using its track ID.    

![image](https://user-images.githubusercontent.com/69602889/184460958-bb31d3ce-6d26-4f7b-94c2-f512ddbb835e.png)    
> [Script](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Spotify/Scripts/getAudioFeatures.py) that uses track IDs to get audio features data for each song    
    
![image](https://user-images.githubusercontent.com/69602889/184462515-5982b458-95eb-4c7b-adda-b5bbc17ad167.png)
> Example of audio features data from Spotify    


The final musical aspects data can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Spotify/Data)       
The scripts for Spotify API queries can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Spotify/Scripts)    

### **Genius Data Collection**

In order to investigate lyrical complexity and lyrical valence (how lyrics convey happiness), I utilized [Genius API](https://pypi.org/project/lyricsgenius/)'s lyrics search features.

![image](https://user-images.githubusercontent.com/69602889/184464142-adaaf546-be67-4d0c-b839-e3a4804a166d.png)
> [Script](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Genius/Scripts/collectLyrics.py) that searches for song lyrics using song and artist name from initial Billboard data

![image](https://user-images.githubusercontent.com/69602889/184498007-7c9d579b-d51b-41ce-9d11-0fa9f3c05952.png)
![image](https://user-images.githubusercontent.com/69602889/184499253-9d05c5da-87d7-4e06-8981-1798c39c0106.png)
> Scripts that clean up lyrics for NLP

The final lyrics data can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Genius/Data)      
The scripts for Genius API queries and cleaning lyrics can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Genius/Scripts)   

[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)

---
## V. Analysis & Results

With all my data collected, I began analysis.

### Music Valence [Spotify and Genius]   
[Lyrical Findings](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Findings/lyricalValence)   
[Audio Findings](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Findings/musicalAspects)   

How has musical valence (the measure of happiness) changed between the eras 2000-2010 and 2010-2020?

### Lyrical Diversity [Findings](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Findings/lyricalDensity) [Genius]
In what ways has the diversity of lyrical content in pop music evolved in the last two decades?

### Elements of Pop [Findings](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Findings/musicalAspects) [Spotify]
Which elements of pop music remained the same throughout the years?
 
### Collaboration [Findings](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Findings/features) [Billboard]
How has the role of collaboration changed between these two decades?

In order to answer this question, I investigated the proportion of songs with feature artists in both decades.  

A quick search revealed that 686 out of 3519 in the 2000s had features (about 19%) and 1409 out of 5364 songs had features (about 26%). Using a [2 Proportion Z-Test](https://github.com/EdwardX29/MusicMeta_DataAnalysis/blob/main/Findings/features/featuresSignificance.ipynb) at the significance level of 0.05 reveals that there is a significant difference between the proportion of songs with collaborators in the 2000s versus the 2010s. **Notably that there is sufficient evidence to conclude that the proportion of songs with features in the 2000s is less than the 2010s.**

![image](https://user-images.githubusercontent.com/69602889/184505514-6394ce92-46c4-43a8-8124-8d3b62d7abf3.png)
![image](https://user-images.githubusercontent.com/69602889/184505508-132fbcef-9cad-4642-bd48-781e60b562dc.png)
     
This shift implies that artists are more inclined to collaborate with one another on songs nowadays. This could be attributed to increased willingness for collaboration in the artists but also could be a reflection of how major music labels have made it easier for artists to make connections in the 2010s.


[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)
   
---
## VI. Discussion & Future Improvements

[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)


