#<<---Seaborn basico--->># (Seaborn esta optimizado para Pandas) (Aun asi toca iniciarlo como Matplotlib)
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid', font_scale=1) #Personalizar el Seaborn
sns.barplot(x=['A','B','C'], y=[1,3,2])
plt.show()