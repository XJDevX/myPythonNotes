#<<---Grafico de barras o Bar Plot--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

country = ['COLOMBIA', 'INDIA', 'CHINA', 'MEXICO', 'GERMANY']
population = [50, 100, 90, 80, 45]

#>> Grafico de barras
plt.bar(country, population, width=0.5, color=['blue', 'green'])
plt.xticks(np.arange(5),('Colombia', 'India', 'China', 'Mexico', 'Alemania'), rotation=45) #Cambiar nombre de categorias
    # plt.barh(country, population) Grafico de barras horizontal
plt.title('Country Popultaion')
plt.xlabel('Country')
plt.ylabel('Population')

plt.show()