#<<---Graficos de categorias de Seaborn--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Graficos
sns.countplot(data=tips, x='day', hue='sex') #Grafico de conteo
plt.show()

sns.stripplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True) #Grafico de dispersion lineal
plt.show()

sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True) #Grafico de dispersion lineal sin sobreposicion
plt.show()

sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True) #Grafico de Box
plt.show()

sns.violinplot(data=tips, x='day', y='total_bill', hue='sex',split=True, dodge=True, palette='pastel') #Similar al box plot pero sin datos estadisticos
plt.show()

sns.catplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True, kind="swarm", col='time') #Similar a displot con 'kind=()'
plt.show()
