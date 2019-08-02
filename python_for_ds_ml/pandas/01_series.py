#%%
import pandas as pd
import numpy as np

#%%
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr= np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

#%%
pd.Series(data=my_data)

#%%
pd.Series(data=my_data, index=labels)

#%%
pd.Series(arr, labels)

#%%
pd.Series(d)

#%%
pd.Series(data=labels)

#%%
pd.Series(data=[sum, print, len])

#%%
ser1 = pd.Series([1, 2, 3, 4],['USA', 'Germany', 'USSR', 'Japan'])

#%%
ser2 = pd.Series([1, 2, 5, 4],['USA', 'Germany', 'Italy', 'Japan'])

#%%
ser3 = pd.Series(data=labels)

#%%
ser3[0]

#%%
ser1

#%%
ser2

#%%
ser1 + ser2

#%%
