#%%
import numpy as np
import pandas as pd

#%%
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)

#%%
by_company = df.groupby('Company')

#%%
by_company.mean()

#%%
by_company.sum().loc['FB']

#%%
df.groupby('Company').mean()

#%%
df.groupby('Company').count()

#%%
df.groupby('Company').max()

#%%
df.groupby('Company').mean()

#%%
df.groupby('Company').describe()

#%%
df.groupby('Company').describe().transpose()['FB']

#%%
