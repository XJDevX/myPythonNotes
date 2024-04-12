#<<---Otros tipos de graficos con Matplotlin--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 90, 100)
plt.style.use('bmh')
fig, axes = plt.subplots(2, 2, figsize=(12, 6), label='Other Graphics')

#>> Histograma
axes[0, 0].hist(data, bins=15)
axes[0, 0].set_title('Histograma')

#>> BoxPlot
axes[1, 0].boxplot(data, patch_artist=True, notch=True, vert=False) #Color al rango intercuartilico y enfasis 
axes[1, 0].set_title('BoxPlot')

#>> Scatter Plot
x = np.random.rand(50) #Variable
y = np.random.rand(50) #Variable
area = (30 * np.random.rand(50)) ** 2 #Variable
colors = np.random.rand(50) #Variable

axes[0, 1].scatter(x, y, s=area, c=colors, alpha=0.7)
axes[0, 1].set_title('Scatter Plot (Aleatorio)')

#>> Grafica de pie
data2 = np.random.rand(20)
axes[1,1].plot(data2, 'bo-')
axes[1,1].set_title('Bar Chart')


fig.tight_layout()
plt.show()