import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import gzip

Tk().withdraw()
path = askopenfilename()

df = pd.read_pickle(path)
print(df)
