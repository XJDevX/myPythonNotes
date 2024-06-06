#<<---Combine charts with Seaborn--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Joinplot
sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', kind='hist', marginal_ticks=True, marginal_kws=dict(bins=25,fill=True,multiple='dodge'))
plt.show()

#>> Pairplot
sns.pairplot(data=tips, hue='sex', kind='scatter', corner=True) #Relation the numeric data and "hue''", makes the separation of them
plt.show()