#<<---Seaborn's more used parameters--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips') #'tips' is an example DF

#>> Charts (Seaborn choices the chart if we don't indicate him in 'kind=')
sns.displot(data=tips, x='total_bill', y='tip', hue='sex', kind='hist', palette='dark') #Histogram
sns.displot(data=tips, x='total_bill', hue='sex', kind='hist', palette='dark') #Histogram
sns.displot(data=tips, x='total_bill', hue='sex', kind='kde', palette='dark') #Distribution by density

#>> Show the chats
plt.show()