#%%
import matplotlib.pyplot as plt


#%%
x = np.linspace(0, 5, 11)
y = x**2
#%%
fig, axes = plt.subplots(nrows=3, ncols=3)
plt.tight_layout()
#%%
fig, axes = plt.subplots(nrows=1, ncols=2)

# for current_ax in axes:
#   current_ax.plot(x, y)
axes[0].plot(x, y)
axes[0].set_title('First Plot')
axes[1].plot(y, x)
axes[1].set_title('Second Plot')


#%%
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
axes[0].plot(x, y)
axes[1].plot(y, x)
plt.tight_layout()
#%%
fig.savefig('my_picture.png', dpi=200)

#%%
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_title('Title')
ax.set_ylabel('Y Label')
ax.set_xlabel('X Label')

#%%
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, x**2, label='X Squared')
ax.plot(x, x**3, label='X Cubed')
# ax.legend(loc=10)
ax.legend(loc=(0.1, 0.1))

#%%
