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
# gender, height - wejścia, dane niezależna
# weight - wyście, dana zależna

# plt.title('Histogram, rozkład weight')
# plt.hist(df.Weight, bins=50)
# plt.show()
#
# plt.hist(df.query("Gender=='Female'").Weight, bins=50)
# plt.title('Histogram, PANIE weight')
# # plt.show()
#
# print('\nHistogram, rozkład PANOWIE weight') # nazwa przykryje wyższą nazwę
# plt.title('Histogram, PANOWIE weight')
# plt.hist(df.query("Gender=='Male'").Weight, bins=50)
# plt.show()
#
# sns.histplot(df.Weight).set_title('Histogram, rozkład weight')
# plt.show()
#
# sns.histplot(df.query("Gender=='Female'").Weight).set_title('Histogram, PANIE weight')
# # plt.show()
# print('\nHistogram, rozkład PANOWIE weight') # nazwa przykryje wyższą nazwę
# sns.histplot(df.query("Gender=='Male'").Weight)
# plt.show()

# zamiana danych na dane numeryczne
df = pd.get_dummies(df)
print(df.head())

#Gender:  0 - mezczyzna, 1 - kobieta
del df['Gender_Male']
print(df.head())
df.rename(columns={'Gender_Female': "Gender"}, inplace=True)
print(df.head())

model = LinearRegression()
model.fit(df[['Height', 'Gender']]  , df['Weight'] )

print(f'Współczynnik kierunkowy: {model.coef_}')
print(f'Wyraz wolny: {model.intercept_}')

print(f'weight = 1.069 * Height + -8.8 * Gender + -102.5')

# Własna formuła
gender = 0
height = 192
weight = model.coef_[0]*height + model.coef_[1]*gender + model.intercept_
print(weight)

# Sprawdzenie
print(model.predict([[192, 0], [167, 1]]))
