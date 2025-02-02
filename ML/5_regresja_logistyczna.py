import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('dane\\diabetes.csv')
print(f'Ile danych: {df.shape}')
print(df.describe().T.to_string())
print('\nLiczba pustych pól:')
print(df.isna().sum())

# wszedzie, gdzie 0 lub brak wartości
# wpisz średnią (bez zer)

# 1. zamień wszystkie 0 na NA
# 2. policz średnią
# 3. wpisz średnią tam, gdzie brak wartości

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col] = df[col].replace(0, np.NaN)
    mean_ = df[col].mean()
    df[col].replace(np.NaN, mean_, inplace=True)   # inplace niedługo niewspierane

print('Po czyszczeniu danych')
print(df.describe().T.to_string())
print(df.isna().sum())



# def myfun(kolor: str, dzien: int, tydzien) -> str:
#     pass
#
#
# myfun('czerwony', 'sroda', 'sdf')
