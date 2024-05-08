import pandas as pd
import numpy as np
from IPython.display import display

# Which ETF performs the best in an economic recession?
# What is the expected rate of growth during the 6 months of recessions for each ETF?

# Import data from CSV for MSFT
spydf = pd.read_csv('SPY Daily Historical 1993.csv')
ratesdf = pd.read_csv('DFF.csv')

# Gain a feel for the data
# display(msftdf.head)
# print(df.tail)
# print(df.shape)
# print(fedratedf.info())

# Look at columns and reduce to ones we care about
# display(fdf.columns)

keep_cols = ['Date','Open','Close','Volume']
drop_cols = spydf.columns.difference(keep_cols)
# print(drop_cols)

spy = spydf.drop(columns=drop_cols)
print(spy)
ratesdf = ratesdf.rename(columns={'DATE':'Date'})
# print('\n'*5)
# print(ratesdf.info())

# Check for Nulls / Duplicates
# msft.groupby("Date").size()

# Merge data frames
df = spy.merge(ratesdf, how="inner", on="Date")
df.to_csv('df.csv', index=False)

# Use regex to clean data
# .str.replace([regex], " ")