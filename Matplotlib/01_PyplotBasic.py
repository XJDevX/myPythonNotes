#<<---PyPlot basico--->>#
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,5,11)
y = x ** 2

#>> Pyplot
plt.plot(x, y, 'ro-') #Primera letra = Color, Segunda letra = Marcador de puntos ('x || o') y '-' continuidad
plt.show()

"""
Al ejecutar y hacer graficas con Matplotlib en VSCode 
debemos importar a parte matplotlib y poner el siguiente
comando para evitar problemas al ejecutarlo en WSL:

    import matplotlib as mpl
    mpl.use('TkAgg')
    
"""

#>> Tipos de graficas
plt.hist(x) #Histograma
plt.show()

plt.pie(x) #Grafica de pie
plt.show()

plt.scatter(x, y) #Scatter plot
plt.show()

plt.boxplot(x) #BoxPlot
plt.show()