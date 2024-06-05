#<<---PyPlot basics--->># (Matplotlib is optimized for NumPy)
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,5,11)
y = x ** 2

#>> Pyplot
plt.plot(x, y, 'ro-') #First letter = Color, Second letter = Point markers ('x' or 'o') and '-' continuity
plt.show()

"""
When whe execute and make charts with Matplotlib in VSCode,
we have to import a part matplotlib and put the following
command to avoid issues when executing in WSL:

    import matplotlib as mlp
    mlp.use('TkAgg)
"""

#>> Types of Charts
plt.hist(x) #Histogram
plt.show()

plt.pie(x) #Pie Chart
plt.show()

plt.scatter(x, y) #Scatter plot
plt.show()

plt.boxplot(x) #BoxPlot
plt.show()