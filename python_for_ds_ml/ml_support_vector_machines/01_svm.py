#%%
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
sns.set_style('whitegrid')
%matplotlib inline

#%%
cancer = load_breast_cancer()
cancer.keys()

#%%
print(cancer['DESCR'])

#%%
df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

#%%
df_feat.head()

#%%
df.info()

#%%
df.describe()

#%%
from sklearn.model_selection import train_test_split
X = df_feat
y = cancer['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#%%
from sklearn.svm import SVC

model = SVC()
model.fit(X_train, y_train)
pred = model.predict(X_test)

#%%
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

#%%
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10, 100, 1000], 'gamma': [1, 0.1, 0.01, 0.001, 0.0001]}
grid = GridSearchCV(SVC(), param_grid, verbose=3)

#%%
grid.fit(X_train, y_train)

#%%
grid.best_params_

#%%
grid.best_estimator_

#%%
grid_pred = grid.predict(X_test)
print(classification_report(y_test, grid_pred))
print(confusion_matrix(y_test, grid_pred))