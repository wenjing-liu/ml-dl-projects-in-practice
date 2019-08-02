# Numpy Excises

#%%
import numpy as np

#%%
np.zeros(10)

#%%
np.ones(10)

#%%
np.ones(10)*5

#%%
np.arange(10, 51)

#%%
np.arange(10,51, 2)

#%%
np.arange(0, 9).reshape(3, 3)

#%%
np.eye(3)

#%%
np.random.rand(1)

#%%
np.random.randn(25)

#%%
np.arange(1, 101).reshape(10, 10)/100

#%%
np.linspace(0, 1, 20)

#%%
mat = np.arange(1, 26).reshape(5, 5)

#%%
mat[2:, 1:]

#%%
mat[3, 4]

#%%
mat[0:3, 1:2]

#%%
mat[4]

#%%
mat[3:]

#%%
np.sum(mat)
mat.sum()

#%%
np.std(mat)
mat.std()

#%%
mat.sum(axis=0)

#%%
