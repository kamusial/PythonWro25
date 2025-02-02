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

df.to_csv('dane\\cukrzyca_po_obrobce.csv', sep=';', index=False)


X = df.iloc[:, :-1]   #wszystkie kolumny, bez ostatniej
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

print('\nLogistic Regression')
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print(f'Zdrowych, ile chorych: {df.outcome.value_counts()}')
print('Zmiana danych')
# 500 zdrowych, 500 chorych

df1 = df.query("outcome==0").sample(n=500)
df2 = df.query(" outcome==1 ").sample(n=500)
df3 = pd.concat([df1, df2])


X = df3.iloc[:, :-1]   #wszystkie kolumny, bez ostatniej
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))


# def myfun(kolor: str, dzien: int, tydzien) -> str:
#     pass
#
#
# myfun('czerwony', 'sroda', 'sdf')
