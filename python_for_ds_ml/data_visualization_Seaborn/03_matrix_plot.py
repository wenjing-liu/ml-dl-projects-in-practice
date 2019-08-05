#%%
import seaborn as sns
%matplotlib inline
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

#%%
flights.head()

#%%
tc = tips.corr()

#%%
sns.heatmap(tc, annot=True, cmap='coolwarm')

#%%
fp = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fp, cmap='magma', linecolor='white', linewidths=3)
#%%
sns.heatmap(fp, cmap='coolwarm', linecolor='black', linewidths=3)

#%%
sns.clustermap(fp, cmap='coolwarm', standard_scale=1)

#%%
