#%%
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set_style('whitegrid')

#%%
titanic = sns.load_dataset('titanic')

#%%
titanic.tail()

#%%
sns.jointplot(x='fare', y='age', data=titanic)

#%%
sns.distplot(titanic['fare'], bins=30, kde=False, color='red')

#%%
sns.boxplot(x='pclass', y='age', data=titanic, palette='rainbow')

#%%
sns.swarmplot(x='pclass', y='age', data=titanic, palette='Set2')

#%%
sns.countplot(x='sex',data=titanic)

#%%
tc =titanic.corr()
sns.heatmap(tc, cmap='coolwarm')
plt.title('titanic.corr()')
#%%
g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')

#%%
