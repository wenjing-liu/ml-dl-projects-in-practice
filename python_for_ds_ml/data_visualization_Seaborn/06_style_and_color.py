#%%
import seaborn as sns
%matplotlib inline
tips = sns.load_dataset('tips')

#%%
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine(left=True, bottom=True)

#%%
plt.figure(figsize=(12, 3))
sns.countplot(x='sex', data=tips)

#%%
sns.set_context('poster')
sns.countplot(x='sex', data=tips)

#%%
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')

#%%
