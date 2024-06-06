#<<---Seaborn's heatmaps--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')

#>> Heatmap
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='crest', linewidths=.5, vmin=.5, vmax=1, cbar=True) #Correlation of the variables
plt.show()