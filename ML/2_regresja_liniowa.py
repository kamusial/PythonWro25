import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('dane\\otodom.csv')
print(df.head(3).to_string()) # 3 piersze wiersze, wszystkie kolumny

print(df.describe().round(2).T.to_string())

print(f'wykres korelacji kolumn')
sns.heatmap(df.iloc[:, 2:].corr(), annot=True)  # wycinay pierwszą kolumne (o indeksie 0)
plt.show()

sns.histplot(df.cena)
plt.show()

plt.scatter(df.powierzchnia, df.cena)
plt.show()

X = df.iloc[ : , 2: ]    # bez 2 pierwszych kolumn
#y = df.iloc[:,1]
y = df.cena
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  #20% danych testowych

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

print(f'Współczynnik kierunkowy: {model.coef_}')
print(pd.DataFrame(model.coef_ , X.columns))

