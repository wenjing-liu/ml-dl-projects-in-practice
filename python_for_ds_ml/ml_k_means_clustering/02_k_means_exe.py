#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set_style('whitegrid')

#%%
df = pd.read_csv('College_Data', index_col=0)

#%%
df.head()

#%%
df.info()

#%%
df.describe()

#%%
sns.scatterplot(x='Room.Board', y='Grad.Rate', data=df, hue='Private', palette='coolwarm')

#%%
sns.lmplot('Room.Board', 'Grad.Rate', data=df, hue='Private', palette='coolwarm', size=6, aspect=1, fit_reg=False)

#%%
sns.lmplot('Outstate', 'F.Undergrad', data=df, hue='Private', palette='coolwarm', size=6, aspect=1, fit_reg=False)

#%%
g = sns.FacetGrid(df, hue='Private', palette='coolwarm', size=6, aspect=2)
g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.7)

#%%
g = sns.FacetGrid(df, hue='Private', palette='coolwarm', size=6, aspect=2)
g = g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.7)

#%%
df[df['Grad.Rate'] > 100]

#%%
df['Grad.Rate']['Cazenovia College'] = 100

#%%
g = sns.FacetGrid(df, hue='Private', palette='coolwarm', size=6, aspect=2)
g = g.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.7)

#%%
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)

#%%
X = df.drop('Private', axis=1)

#%%
kmeans.fit(X)

#%%
kmeans.cluster_centers_

#%%
kmeans.labels_

#%%
df['Cluster'] = df['Private'].apply(lambda x: 1 if x=='Yes' else 0)

#%%
df.head()

#%%
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(df['Cluster'], kmeans.labels_))
print(confusion_matrix(df['Cluster'], kmeans.labels_))

#%%
