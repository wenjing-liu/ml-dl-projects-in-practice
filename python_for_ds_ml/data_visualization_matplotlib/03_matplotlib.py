#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
x = np.linspace(0, 5, 11)
y = x**2

#%%
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
# ax.plot(x, y, color='blue')
# ax.plot(x, y, color='#FF8C00') # RGB Hex Code
# ax.plot(x, y, color='purple', linewidth=3, alpha=0.5)
# ax.plot(x, y, color='purple', lw=3, alpha=0.5)
# ax.plot(x, y, color='purple', linewidth=3, linestyle='-.')
# ax.plot(x, y, color='purple', lw=3, ls='-.')
# ax.plot(x, y, color='purple', linewidth=3, linestyle='-', marker='+')
# ax.plot(x, y, color='purple', linewidth=3, linestyle='-', marker='o', markersize=20, markerfacecolor='yellow', markeredgewidth=3)
ax.plot(x, y, color='purple', linewidth=2, linestyle='--')
ax.set_xlim([0, 1])
ax.set_ylim([0, 2])
#%%


#%%
