#<<---Subplots with MOO--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = np.sin(x)

#>> Charts
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2) #Define previously the axis or charts
ax1.plot(x, y, 'bD--') #Charts can be easily modifiable
ax2.plot(y, x, 'rx-')
plt.show()

#>> Other chart
fig, axes = plt.subplots(2, 4) #Define previously the axis or charts
axes[0,0].plot(x, np.cos(x), 'yo-')
axes[0,1].plot(x, np.sin(x), 'bx-')
axes[0,2].plot(x, np.tan(x), 'rD--')
axes[0,3].plot(x, np.cos(x) ** 2)

fig.tight_layout() #Boost the visibility ob the axis
plt.show()