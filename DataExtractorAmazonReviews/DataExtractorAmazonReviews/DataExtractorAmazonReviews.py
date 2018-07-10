#https://zenodo.org/record/1000885#.W0OO0tJKiUl is the source of the steam review data set
#http://ai.stanford.edu/~amaas/data/sentiment/ for movie reviews

#Amazon Reviews data set
# R. He, J. McAuley. Modeling the visual evolution of fashion trends with one-class collaborative filtering. WWW, 2016
# J. McAuley, C. Targett, J. Shi, A. van den Hengel. Image-based recommendations on styles and substitutes. SIGIR, 2015
#

import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os
import json
import gzip

#Used on Amazon Reviews:
def parse(path):
    # Access the json.gz
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
  i = 0
  df = {}
  print('Began parsing ', name)
  # Update the dataframe
  for d in parse(path):
    df[i] = d
    i += 1
    if (i % 10) == 0:
        print('Parsed ', i, 'reviews from ', path)
  # Drop unneeded columns and return the data frame with just review text and ratings
  #df.drop(columns=['reviewerID','asin','reviewerName','helpful','summary','unixTimeReview','reviewTime'])
  return pd.DataFrame.from_dict(df, orient='index')

# Select directory
Tk().withdraw()
directory = askdirectory()

n = 0
files = {}

for root, dirs, files in os.walk(str(directory)):
    for name in files:
        files[n] = os.path.join(root, name)
        print('Completed entering file: ', name)

# Go through directory
for review in files:
    # Get name of review category
    reviewString = str(review)[8 : -8]
    # Save to pd data frame
    df = getDF(str(review))
    print(df)
    # Save data frame to a pickle
    #df.to_pickle("C:/TrainingData/amazon_pickles/" + reviewString + ".pkl")



#Used on Stanford Movie Reviews Dataset



#Used on Steam Reviews:
#Tk().withdraw()
#path = askopenfilename()
#df = pd.read_csv(path, names=["ID","Review_Text","Positive", "Negative"])
#df.drop(columns=['ID'])
#
#print("Read the csv")
#
#print(df)
#
#df.to_pickle("C:/TrainingData/steam_reviews_pickled.pkl")
#print("Done!")