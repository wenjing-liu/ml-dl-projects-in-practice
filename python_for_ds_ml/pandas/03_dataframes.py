#%%
import numpy as np
import pandas as pd
from numpy.random import randn

#%%
np.random.seed(101)

#%%
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

#%%
df > 0

#%%
df[df>0]

#%%
df['W'] > 0

#%%
resultdf = df[df['W']>0][['X','Y']]

#%%
resultdf

#%%
df[(df['W']> 0) | (df['Y'] > 0.1)]

#%%
df.reset_index()

#%%
newind = 'CA NY WY OR CO'.split()

#%%
df['States'] = newind

#%%
df.set_index('States')

#%%
