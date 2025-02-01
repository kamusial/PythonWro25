import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC  #clasifiaer
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('dane\\heart.csv', comment='#')
print(df)

X = df.iloc[:, :-1]   #wszystkie kolumny, bez ostatniej
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

print('\nLogistic Regression')
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nKNN')
model = KNeighborsClassifier(n_neighbors=5) #, weights='distance')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nDrzewo decyzyjne')
model1 = DecisionTreeClassifier(max_depth=30, min_samples_split=2)
model1.fit(X_train, y_train)
print(model1.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model1.predict(X_test))))

print('\nSVC')
model = SVC()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
