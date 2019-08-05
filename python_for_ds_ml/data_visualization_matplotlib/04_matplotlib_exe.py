#%%
import numpy as np
x = np.arange(0, 100)
y = x*2
z = x**2

#%%
import matplotlib.pyplot as plt

%matplotlib inline

#%%
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_title('Title')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

#%%
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, .2, .2])
ax1.plot(x, y)
ax2.plot(x, y)

#%%
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, .4, .4])
ax1.plot(x, z)
ax2.plot(x, y)
ax2.set_xlim(20, 22)
ax2.set_ylim(30, 50)
#%%
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
axes[0].plot(x, y, ls='--',lw=2)
axes[1].plot(x, z, color='red', lw=4)

#%%
