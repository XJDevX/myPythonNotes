#<<---Seaborn's distribution charts--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Distribution charts
sns.histplot(data=tips, x='tip', bins=15, cumulative=False, hue='sex', stat='count', multiple='dodge') #Histogram
plt.show()

sns.kdeplot(data=tips, x='tip', hue='sex', cumulative=False, shade=True, bw_adjust=1) #Density chart
plt.show()

sns.ecdfplot(data=tips, x='tip', hue='sex', stat='count') #Step chart
plt.show()

#>> Displot
sns.displot(data=tips, x='tip', hue='sex', kind='hist', multiple='stack') #Similar to a Histogram
plt.show()