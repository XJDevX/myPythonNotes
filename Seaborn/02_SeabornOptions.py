#<<---Parametros mas usados de Seaborn--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips') #'tips' es un DF de ejemplo

#>> Graficos (Seaborn elige el grafico si no se lo indicamos en 'kind=')
sns.displot(data=tips, x='total_bill', y='tip', hue='sex', kind='hist', palette='dark') #Histograma
sns.displot(data=tips, x='total_bill', hue='sex', kind='hist', palette='dark') #Histograma
sns.displot(data=tips, x='total_bill', hue='sex', kind='kde', palette='dark') #Distribucion por densidad

#>> Fin de los graficos
plt.show()