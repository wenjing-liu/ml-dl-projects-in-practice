#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
%matplotlib inline

#%%
df = pd.read_csv('KNN_Project_Data')

#%%
df.head()

#%%
sns.pairplot(df, hue='TARGET CLASS', diag_kind='hist')

#%%
scalar = StandardScaler()
scalar.fit(df.drop('TARGET CLASS', axis=1))
scaled_feature = scalar.transform(df.drop('TARGET CLASS', axis=1))
df_feature = pd.DataFrame(scaled_feature, columns=df.columns[:-1])

#%%
X = df_feature
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#%%
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

#%%
error_rate = []

for i in range(1, 40):
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(X_train, y_train)
  pred_i = knn.predict(X_test)
  error_rate.append(np.mean(pred_i != y_test))

sns.set_style('whitegrid')
plt.Figure(figsize=(10, 6))
plt.plot(range(1, 40), error_rate, color='blue', ls='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate with K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

#%%
knn = KNeighborsClassifier(n_neighbors=31)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

#%%
