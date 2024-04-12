#<<---Personalizacion de graficos--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = np.sin(x)

#>> Hacer graficos
fig, axes = plt.subplots(1, 2, figsize=(8,5))
axes[0].plot(x, y, 'bD--', label='$sin(x)$') #Se definen los labels en la grafica, ($-$) -> Notacion Matematica
axes[1].plot(y, x, 'ro-', label='$sin(x)$')

#>> Personalizar graficos
axes[0].set_title('Relacion X - Y') #Poner titulos a los axes
axes[1].set_title('Relacion Y - X')

axes[0].set_xlabel('X') #Poner titulos a los axis o labels
axes[0].set_ylabel('Y')
axes[1].set_xlabel('Y')
axes[1].set_ylabel('X')

axes[0].legend(loc='lower left') #Aplicar labels que se definen en el grafico, (loc='') -> Ubicacion de 'legend'
axes[1].legend(loc='lower left')

plt.show()