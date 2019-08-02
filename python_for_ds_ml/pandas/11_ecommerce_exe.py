#%%
import pandas as pd

#%%
df = pd.read_csv('Ecommerce Purchases')

#%%
df.head()

#%%
df.info()

#%%
df['Purchase Price'].mean()

#%%
df['Purchase Price'].max()

#%%
df['Purchase Price'].min()

#%%
df[df['Language'] == 'en'].count()

#%%
df[df['Job'] == 'Lawyer'].count()

#%%
df['AM or PM'].value_counts()

#%%
df['Job'].value_counts().head(5)

#%%
df[df['Lot'] == '90 WT']['Purchase Price']

#%%
df[df["Credit Card"] == 4926535242672853]['Email']

#%%
df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)].count()

#%%
sum(df['CC Exp Date'].apply(lambda x: x[3:]) == '25')

#%%
df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

#%%
