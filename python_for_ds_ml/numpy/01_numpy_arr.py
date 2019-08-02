# NumPy Arrays
#%%
import numpy as np

my_list = [1, 2, 3]
arr_list = np.array(my_list)
#%%
my_mat = [[1,2,3], [4,5,6],[7,8,9]]


#%%
np.array(my_mat)

#%%
np.arange(0, 11, 2)

#%%
np.zeros(3)

#%%
np.zeros((2, 3))

#%%
np.ones(4)

#%%
np.ones((3,4))

#%%
np.linspace(0, 5, 10)

#%%
np.eye(4)

#%%
np.random.rand(5)

#%%
np.random.rand(5,5)

#%%
np.random.randn(2)

#%%
np.random.randn(4,4)

#%%
np.random.randint(1, 100)

#%%
np.random.randint(1, 100, 10)

#%%
arr = np.arange(25)

#%%
ranarr= np.random.randint(0, 50, 10)

#%%
arr.reshape(5, 5)

#%%
ranarr.max()

#%%
ranarr.min()

#%%
ranarr.argmax()

#%%
ranarr.argmin()

#%%
arr.shape

#%%
ranarr.shape

#%%
arr = arr.reshape(5, 5)

#%%
arr.shape

#%%
arr.dtype

#%%
from numpy.random import randint
randint(2, 10, 3)

#%%
