#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline
sns.set_style('whitegrid')

#%%
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
type(cancer)

#%%
cancer.keys()

#%%
print(cancer['DESCR'])

#%%
df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

#%%
df.head()

#%%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

#%%
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

#%%
scaled_data.shape

#%%
x_pca.shape

#%%
plt.figure(figsize=(8, 6))
plt.scatter(x_pca[:,0], x_pca[:, 1], c=cancer['target'], cmap='plasma')
plt.xlabel('First Principle Component')
plt.ylabel('Second Principle Component')

#%%
pca.components_

#%%
df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])
df_comp

#%%
sns.heatmap(df_comp, cmap='plasma')

#%%
