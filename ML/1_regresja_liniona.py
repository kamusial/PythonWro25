import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression  # scikit-learn

print('hello')

df = pd.read_csv('dane\\weight-height.csv', sep=';')
print(f'typ: {type(df)}')
print(df)
print(f'3 pierwse wiersze \n{df.head(3)}')
print(f'kolumny: {df.columns}')
print(f'kształt {df.shape}')
print(f'Ile pań i ile panów: {df.Gender.value_counts()}')
df.Height *= 2.54
df.Weight /= 2.2
print(f'Dane po zmianie jednostek\n{df.head()}')
