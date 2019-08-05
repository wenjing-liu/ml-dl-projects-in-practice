#%%
import seaborn as sns
%matplotlib inline

#%%
tips = sns.load_dataset('tips')

#%%
tips.head()

#%%
sns.distplot(tips['total_bill'], kde=False, bins=30)

#%%
# sns.jointplot(x='total_bill', y='tip', data=tips)
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')

#%%
# sns.pairplot(tips)
# sns.pairplot(tips, hue='sex')
sns.pairplot(tips, hue='sex', palette='coolwarm')

#%%
sns.rugplot(tips['total_bill'])

#%%
sns.kdeplot(tips['total_bill'])


#%%
