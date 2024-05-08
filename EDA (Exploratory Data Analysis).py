import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('df.csv')
print(df.describe())

# Correlation Matrix