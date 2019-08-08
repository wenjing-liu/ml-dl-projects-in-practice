#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
%matplotlib inline
sns.set_style('whitegrid')

#%%
ad_data = pd.read_csv('advertising.csv')

#%%
ad_data.head()

#%%
ad_data.info()

#%%
ad_data.describe()

#%%
sns.distplot(ad_data['Age'].dropna(), kde=False, bins=20)

#%%
sns.jointplot(x='Age', y='Area Income', data=ad_data)

#%%
sns.jointplot(x='Age', y='Daily Time Spent on Site', data=ad_data, kind='kde')

#%%
sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=ad_data)

#%%
sns.pairplot(ad_data, hue='Clicked on Ad', palette='bwr', diag_kind='hist')

#%%
ad_data.columns

#%%
X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income',
'Daily Internet Usage', 'Male']]

y = ad_data['Clicked on Ad']

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#%%
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

#%%
predictions = logmodel.predict(X_test)

#%%
print(classification_report(y_test, predictions))

#%%
confusion_matrix(y_test, predictions)

#%%
