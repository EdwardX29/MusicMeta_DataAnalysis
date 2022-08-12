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
5. [Results](#v-results)
6. [Discussion](#vi-discussion--future-improvements)
7. [Usage](#vii-usage)
   

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

> The final organized data can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Billboard/Data)   
> The data collection and data preprocessing scripts can be found [here](https://github.com/EdwardX29/MusicMeta_DataAnalysis/tree/main/Billboard/Data)

### **Spotify Data Collection**

### **Genius Data Collection**


[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)

---
## V. Results
[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)
   
---
## VI. Discussion & Future Improvements

[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)

---
## VII. Usage
   
[top](#musical-metamorphasis-a-study-of-the-evolution-of-popular-music-2000s--2010s)
