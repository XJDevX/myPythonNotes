#<<---Seaborn's category charts--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Charts
sns.countplot(data=tips, x='day', hue='sex') #Chart of count
plt.show()

sns.stripplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True) #Linear dispersion chart
plt.show()

sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True) #Linear dispersion chart without superposition
plt.show()

sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True) #Box chart
plt.show()

sns.violinplot(data=tips, x='day', y='total_bill', hue='sex',split=True, dodge=True, palette='pastel') #Similar to Box chart but without stadistic data
plt.show()

sns.catplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True, kind="swarm", col='time') #Similar to Displot with 'kind='
plt.show()
