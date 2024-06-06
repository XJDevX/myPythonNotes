#<<---Seaborn's basics--->># (Seaborn is optimized for Pandas) (Even so we have to call it like Matplotlib)
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid', font_scale=1) #Personalize the Seaborn
sns.barplot(x=['A','B','C'], y=[1,3,2])
plt.show()