#https://zenodo.org/record/1000885#.W0OO0tJKiUl is the source of the steam review data set
#http://ai.stanford.edu/~amaas/data/sentiment/ for movie reviews

import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import gzip

Tk().withdraw()
path = askopenfilename()
df = pd.read_csv(path, names=["ID","Review_Text","Positive", "Negative"])
df.drop(columns=['ID'])

print("Read the csv")

print(df)

df.to_pickle("C:/TrainingData/steam_reviews_pickled.pkl")
print("Done!")