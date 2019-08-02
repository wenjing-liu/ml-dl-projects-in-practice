#%%
import numpy as np
import pandas as pd

#%%
d = {
  'A': [1, 2, np.nan],
  'B': [5, np.nan, np.nan],
  'C': [1, 2, 3]
}
df = pd.DataFrame(d)

#%%
df.dropna(axis=1)
#%%
df.dropna(thresh=2)

#%%
df['A'].fillna(value=df['A'].mean())

#%%
