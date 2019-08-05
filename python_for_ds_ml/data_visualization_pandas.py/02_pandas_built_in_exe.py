#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set_style('whitegrid')
df3 = pd.read_csv('df3')

#%%
df3.info()

#%%
df3.tail()

#%%
df3.plot.scatter(x='a', y='b', c='red', s=50, figsize=(12, 3))

#%%
df3['a'].plot.hist(bins=30)

#%%
plt.style.use('ggplot')

#%%
df3['a'].plot.hist(alpha=0.5, bins=25)

#%%
df3[['a', 'b']].plot.box()

#%%
df3['d'].plot.kde()

#%%
df3['d'].plot.density()

#%%
df3['d'].plot.kde(ls='--', lw=2)

#%%
df3.iloc[0:31].plot.area(alpha=0.4)

#%%
f = plt.figure()
df3.iloc[0:31].plot.area(alpha=0.4, ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()

#%%
