#%%
import seaborn as sns
import numpy as np
%matplotlib inline
tips = sns.load_dataset('tips')

#%%
sns.barplot(x='sex', y='total_bill', data=tips)

#%%
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

#%%
sns.countplot(x='sex', data=tips)

#%%
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

#%%
sns.violinplot(x='day', y='total_bill', data=tips)

#%%
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')

#%%
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

#%%
sns.stripplot(x='day', y='total_bill', data=tips)

#%%
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

#%%
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)

#%%
sns.swarmplot(x='day', y='total_bill', data=tips)

#%%
sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')

#%%
