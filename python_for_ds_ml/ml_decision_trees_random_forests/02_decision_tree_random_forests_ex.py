#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
%matplotlib inline
sns.set_style('whitegrid')

#%%
loans = pd.read_csv('loan_data.csv')

#%%
loans.head(5)

#%%
loans.info()

#%%
loans.describe()

#%%
plt.Figure(figsize=(10, 6))
loans[loans['credit.policy'] == 1]['fico'].hist(alpha=0.5,color='blue', bins=30,label='Credit.Policy=1')
loans[loans['credit.policy'] == 0]['fico'].hist(alpha=0.5, color='red', bins=30,label='Credit.Policy=0')
plt.legend()
plt.xlabel('FICO')
#%%
plt.Figure(figsize=(10, 6))
loans[loans['not.fully.paid'] == 1]['fico'].hist(alpha=0.5,color='blue', bins=30,label='not.fully.paid=1')
loans[loans['not.fully.paid'] == 0]['fico'].hist(alpha=0.5, color='red', bins=30,label='not.fully.paid=0')
plt.legend()
plt.xlabel('FICO')

#%%
plt.Figure(figsize=(15, 7))
sns.countplot(x='purpose', data=loans, hue='not.fully.paid', palette='Set1')

#%%
sns.jointplot(x='fico', y='int.rate', data=loans)

#%%
plt.figure(figsize=(11,7))
sns.lmplot(y='int.rate',x='fico',data=loans,hue='credit.policy',
           col='not.fully.paid',palette='Set1')

#%%
cat_feats = ['purpose']

#%%
final_data = pd.get_dummies(loans, columns=cat_feats, drop_first=True)

#%%
final_data.head()

#%%
final_data.info()

#%%
X = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
pred = dtree.predict(X_test)
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

#%%
rfc = RandomForestClassifier(n_estimators=600)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print(classification_report(y_test, rfc_pred))
print(confusion_matrix(y_test, rfc_pred))
#%%
