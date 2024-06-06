#<<---Seaborn's relations charts--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Charts
plt.figure(figsize=(12, 5))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time', size='size')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

plt.figure(figsize=(12, 5))
sns.lineplot(data=tips, x='total_bill', y='tip', hue='day', style='time', size='size')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

plt.figure(figsize=(12, 5))
sns.relplot(data=tips, x='total_bill', y='tip', hue='day', style='time', size='size', kind="line", col='time') #Similar to Displot or Catplot
plt.show()