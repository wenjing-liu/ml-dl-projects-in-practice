#%%
import numpy as np
import pandas as pd
import seaborn as sns
%matplotlib inline

df1 = pd.read_csv('df1', index_col=0)

#%%
df1.head()

#%%
df2= pd.read_csv('df2')
#%%
df2.head()

#%%
df1['A'].hist(bins=30)

#%%
# df1['A'].plot(kind='hist', bins=30)
df1['A'].plot.hist()
#%%
df2.plot.area(alpha=0.4)

#%%
df2.plot.bar(stacked=True)

#%%
df1['A'].plot.hist(bins=50)

#%%
df1.plot.line(x='A',y='B',figsize=(12,3),lw=1)

#%%
df1.plot.scatter(x='A',y='B')

#%%
type(df1.index.to_series())

#%%
type(df1['B'])

#%%
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')

#%%
df1.plot.scatter(x='A', y='B', s=df1['C']*100)

#%%
df2.plot.box()

#%%
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])

#%%
df

#%%
df.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')

#%%
df2['a'].plot.kde()

#%%
df2['a'].plot.density()

#%%
df2.plot.density()

#%%
