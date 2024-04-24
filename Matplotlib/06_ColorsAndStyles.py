#<<---Personalizacion de graficos y sus colores--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 11)

plt.style.use('bmh') #Aplicar estilos, 'bmh' = Grilla de los valores
plt.style.use('dark_background')
fig, ax = plt.subplots(1, 2, figsize=(10,5))

#Modificaciones del tipo Matlab
ax[0].set_title('MatLab')
ax[0].plot(x, x*2, 'yo--')
ax[0].plot(x, x*3, 'bx-')
ax[0].plot(x, x*4, 'gv-.')
ax[0].plot(x, x*5, 'rD:')

#Modificaciones con Pyplot
ax[1].set_title('PyPlot')
ax[1].plot(x, x*2, color='yellow', linewidth=2, linestyle="--", marker='o', markersize=4, markerfacecolor="white")
ax[1].plot(x, x*3, color='blue', linewidth=2, linestyle='-', marker='x', markersize=5, markerfacecolor="white")
ax[1].plot(x, x*4, color='green', linewidth=2, linestyle='dashdot', marker='v', markersize=6, markerfacecolor="white")
ax[1].plot(x, x*5, color='#FF0000', linewidth=2, linestyle=':', marker='D', markersize=7, markerfacecolor="white")
#Se pueden poner colores en formato RGB

plt.show()