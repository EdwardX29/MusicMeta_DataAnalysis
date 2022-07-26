# Imports #
import json 
# import matplotlib
import numpy
from scipy.stats import *

# Class Definition # 

class Analyse:

  def __init__(self, year):
    self.year = year

  def getTotalSongs(self):
    with open(f"Data/{self.year}sSpecificData/features{self.year}.json", "r") as f:
      contents = json.load(f)

    return len(contents)

  def getTotalArtists(self):
    return len(self.getArtists())

  def getArtists(self):
    with open(f"Data/{self.year}sSpecificData/features{self.year}.json", "r") as f:
      contents =json.load(f)
    unique = set()
    for dict in contents:
      unique.add(dict["author"])
    return list(unique)
  
  '''
  --------------------------
  Features Methods Begin Here
  '''
  def getTotalFeatures(self):
    with open(f"Data/{self.year}sSpecificData/features{self.year}.json", "r") as f:
      contents = json.load(f)
    featureCount = 0
    for dict in contents:
      if dict["featuring"] != "":
        featureCount+=1
    return featureCount
    
  '''
  -------------------------
  Dictionary Methods Begin Here
  '''
  
  def getDict(self, dictName):
    with open(f"Data/{self.year}sSpecificData/{dictName}{self.year}.json", "r") as f:
      contents = json.load(f)
    return contents

  def getFrequenciesDict(self, dict):
    d = {}
    total = sum(dict.values())
    for key, value in dict.items():
      d[key] = round(value/total, 3)
    return d

  '''
  -------------------------------
  List Methods Begin Here
  '''
  def getList(self, listName):
    with open(f"Data/{self.year}sSpecificData/{listName}{self.year}.json", "r") as f:
      contents = json.load(f)
    return contents
  
  def getAvgList(self, list):
    return numpy.mean(list)

  def getMedianList(self, list):
    return numpy.median(list)

  def getIQRList(self, list):
    return numpy.percentile(list, 75) - numpy.percentile(list, 25)

  def getSTDList(self, list):
    return numpy.std(list)
    
