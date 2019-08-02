#%%
import pandas as pd

#%%
df = pd.read_csv('./example')
#%%
df.to_csv('my_output', index=False)
#%%
pd.read_csv('my_output')

#%%
df = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1', index_col=0)

#%%
df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

#%%
data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

#%%
data[0].head()

#%%
from sqlalchemy import create_engine

#%%
engine = create_engine('sqlite:///:memory:')

#%%
df.to_sql('my_table', engine)

#%%
sqldf = pd.read_sql('my_table', con=engine)

#%%
sqldf

#%%
