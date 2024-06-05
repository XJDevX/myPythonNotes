#<<---Charts personalization--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = np.sin(x)

#>> Make charts
fig, axes = plt.subplots(1, 2, figsize=(8,5))
axes[0].plot(x, y, 'bD--', label='$sin(x)$') #Labels of the chart, ($-$) -> Mathematical Notation
axes[1].plot(y, x, 'ro-', label='$sin(x)$')

#>> Personalize charts
axes[0].set_title('Relacion X - Y') #Put title to the axis
axes[1].set_title('Relacion Y - X')

axes[0].set_xlabel('X') #Put title to the axis
axes[0].set_ylabel('Y')
axes[1].set_xlabel('Y')
axes[1].set_ylabel('X')

axes[0].legend(loc='lower left') #Apply labels that are defined in the chart, (loc='') -> Ubication of the 'legend'
axes[1].legend(loc='lower left')

plt.show()