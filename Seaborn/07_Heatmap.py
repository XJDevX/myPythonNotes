#<<---Graficos de calor con Seaborn--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Heatmap o mapa de calor
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='crest', linewidths=.5,
            vmin=.5, vmax=1, cbar=True) #Correlacion de las variables
plt.show()