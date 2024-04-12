#<<---Metodo orientado a objetos (Combinar graficos)--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#>> Graficos con Moo es muy bueno porque es sencillo de personalizar
fig = plt.figure() #Crear un 'Lienzo' para graficar :)
axes = fig.add_axes([0.1,0.1,0.8,0.9]) #Primeros dos numeros -> (Distancia desde el borde o los ejes)
axes2 = fig.add_axes([0.2,0.55,0.4,0.3]) #Ultimos dos numeros -> (Tamaño del grafico y las axis)
axes2.set_facecolor('gray')

axes.plot(x, y, 'bD-')
axes2.plot(y, x, 'r--')
plt.show()