import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('dane\\otodom.csv')

print(df.iloc[  3:16  ,  2:5  ])

print(df.loc[:, 'liczba_pieter'])