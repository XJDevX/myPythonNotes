#<<---Subplots con el metodo MOO--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = np.sin(x)

#>> Graficos
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2) #Definir previamente los axes o graficos
ax1.plot(x, y, 'bD--') #Graficos pueden ser personalizados facilmente
ax2.plot(y, x, 'rx-')
plt.show()

#>> Otro grafico
fig, axes = plt.subplots(2, 4) #Definir previamente los axes o graficos
axes[0,0].plot(x, np.cos(x), 'yo-')
axes[0,1].plot(x, np.sin(x), 'bx-')
axes[0,2].plot(x, np.tan(x), 'rD--')
axes[0,3].plot(x, np.cos(x) ** 2)

fig.tight_layout() #Mejorar la visibilidad de los axes
plt.show()