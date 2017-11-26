"""
Using pandas to read in a dataframe from a csv-file.
"""

import pandas as pd         # use the pandas library, conventionally named as pd

df = pd.read_csv('testdata.csv')     # Read in file 'testdata.csv' as a dataframe

print df.head()                   # Display first five rows of dataframe
