#<<---Bar Plot--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

country = ['COLOMBIA', 'INDIA', 'CHINA', 'MEXICO', 'GERMANY']
population = [50, 100, 90, 80, 45]

#>> Bar chart
plt.bar(country, population, width=0.5, color=['blue', 'green'])
plt.xticks(np.arange(5),('Colombia', 'India', 'China', 'Mexico', 'Germany'), rotation=45) #Change the name of the categories
    # plt.barh(country, population) #Horizontal Bar chart
plt.title('Country Popultaion')
plt.xlabel('Country')
plt.ylabel('Population')

plt.show()