#<<---Subplot--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#>> Graficos (Con Subplot o varios graficos)
plt.subplot(2, 1, 1)
plt.plot(x, y, 'r--')
plt.plot(y, x, 'b:')
plt.subplot(2, 1, 2)
plt.pie(x)
plt.show()