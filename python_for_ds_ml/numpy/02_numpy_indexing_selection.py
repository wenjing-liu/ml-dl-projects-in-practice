# Numpy Indexing and Selection
#%%
import numpy as np

#%%
arr = np.arange(0, 11)

#%%
arr[8]

#%%
arr[1:5]

#%%
arr[0:5]

#%%
arr[0:6]

#%%
arr[5:]

#%%
arr[0:5]=100

#%%
arr = np.arange(0, 11)

#%%
slice_of_arr = arr[0:6]

#%%
slice_of_arr[:] = 99

#%%
arr

#%%
arr_copy = arr.copy()

#%%
arr_copy[:] = 100

#%%
arr

#%%
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

#%%
arr_2d[0][0]

#%%
arr_2d[0]

#%%
arr_2d[1][1]

#%%
arr_2d[2][1]

#%%
arr_2d[2, 1]

#%%
arr_2d[1,]

#%%
arr_2d[:2,1:]

#%%
arr = np.arange(1, 11)

#%%
bool_arr = arr > 5

#%%
arr[bool_arr]

#%%
arr[arr>5]

#%%
arr[arr<3]

#%%
arr_2d = np.arange(50).reshape(5, 10)

#%%
arr_2d[1:3, 3:5]

#%%
