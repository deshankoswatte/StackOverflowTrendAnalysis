# Adding all the imports
# import warnings
# import itertools
# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# import statsmodels.api as sm
import matplotlib
# import json

# Initializing matplotlib parameters
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

# url = 'https://drive.google.com/open?id=1KhRlMBLA4I6G08nqjH63fOBiSxz5WBzV'
path = 'data/StackOverflowTagsUpdated.csv'

data = pd.read_csv(path, parse_dates=['date'])
# Dataset is now stored in a Pandas Dataframe

# Print overview of the dataset
data.head()

data.describe()
