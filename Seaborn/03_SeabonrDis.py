#<<---Graficos de distribucion de Seaborn--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Graficos de distribucion
sns.histplot(data=tips, x='tip', bins=15, cumulative=False, hue='sex', stat='count', multiple='dodge')
plt.show()

sns.kdeplot(data=tips, x='tip', hue='sex', cumulative=False, shade=True, bw_adjust=1) #Diagrama de densidad
plt.show()

sns.ecdfplot(data=tips, x='tip', hue='sex', stat='count') #Grafico escalonado
plt.show()

#>> Usar Displot
sns.displot(data=tips, x='tip', hue='sex', kind='hist', multiple='stack')
plt.show()