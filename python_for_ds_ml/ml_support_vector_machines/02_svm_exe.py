#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix

sns.set_style('whitegrid')
%matplotlib inline
#%%
from IPython.display import Image
url = 'http://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg'
Image(url,width=300, height=300)

#%%
# The Iris Versicolor
from IPython.display import Image
url = 'http://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg'
Image(url,width=300, height=300)

#%%
# The Iris Virginica
from IPython.display import Image
url = 'http://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg'
Image(url,width=300, height=300)

#%%
iris = sns.load_dataset('iris')

#%%
iris.head()

#%%
iris.info()

#%%
iris.describe()

#%%
sns.pairplot(iris, hue='species', diag_kind='hist', palette='Dark2')

#%%
setosa = iris[iris['species']=='setosa']
sns.kdeplot(setosa['sepal_width'], setosa['sepal_length'], cmap="plasma", shade=True, shade_lowest=False)

#%%
X = iris.drop('species', axis=1)
y = iris['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#%%
svc = SVC()
svc.fit(X_train, y_train)
pred = svc.predict(X_test)

#%%
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
#%%
param_grid = {'C':[0.1, 1, 10, 100, 1000], 'gamma':[1, 0.1, 0.01, 0.001, 0.0001]}
grid = GridSearchCV(SVC(), param_grid, verbose=3)
grid.fit(X_train, y_train)
grid_pred = grid.predict(X_test)

#%%
print(classification_report(y_test, grid_pred))
print(confusion_matrix(y_test, grid_pred))

#%%
grid.best_params_

#%%
grid.best_estimator_

#%%
