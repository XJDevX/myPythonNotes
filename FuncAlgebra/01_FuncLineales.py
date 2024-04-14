#<<---Funciones algebraicas lineales--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#>> Funcion lineal:
n = 100 #Resolucion o puntos que tenemos en la grafica

def f(x, m, b): #Funcion de la grafica
    return m * x + b

x = np.linspace(-10, 10, n) #Crear 10 numeros de -10 a 10
y = f(x, 10, 5) #Funcion f(x)

#>> Grafica de la funcion
fig, ax = plt.subplots(label='Funciones algebraicas')
ax.plot(x, y, label="$f(x) = mx + b$")
ax.set_title('Funcion lineal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(loc='upper left')
ax.grid()

plt.show() #Mostrar grafica