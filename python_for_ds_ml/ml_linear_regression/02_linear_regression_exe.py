#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set_style('whitegrid')

#%%
df = pd.read_csv('Ecommerce Customers')

#%%
df.info()

#%%
df.head()

#%%

df = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']]
#%%
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=df)

#%%
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=df)

#%%
sns.jointplot(x='Time on App', y='Length of Membership', data=df, kind='hex')

#%%
df.head()


#%%
sns.pairplot(df)

#%%
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=df)

#%%
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

#%%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#%%
lm = LinearRegression()

#%%
lm.fit(X_train, y_train)
lm.intercept_
lm.coef_
#%%
predictions = lm.predict(X_test)


#%%
plt.scatter(y_test, predictions)
plt.xlabel('Y test')
plt.ylabel('Predicted Y')

#%%
from sklearn import metrics
metrics.mean_absolute_error(y_test, predictions)
metrics.mean_squared_error(y_test, predictions)
np.sqrt(metrics.mean_squared_error(y_test, predictions))

#%%
sns.distplot((y_test - predictions), bins=50)

#%%
coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients

#%%
