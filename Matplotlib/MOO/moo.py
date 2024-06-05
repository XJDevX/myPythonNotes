#<<---Method Oriented to Objects (Combine charts)--->>#
import matplotlib as mlp
mlp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#>> The charts with MOO is really great because is easy to use and personalize
fig = plt.figure() #Create a 'Canvas' to make charts
axes = fig.add_axes([0.1,0.1,0.8,0.9]) #First two numbers -> (Distance from the border or the axis)
axes2 = fig.add_axes([0.2,0.55,0.4,0.3]) #Las two numbers -> (Size of the chart and the axis) 
axes2.set_facecolor('gray')

axes.plot(x, y, 'bD-')
axes2.plot(y, x, 'r--')
plt.show()