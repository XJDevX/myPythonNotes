#<<---Creating Arrays with Numpy--->>#
import numpy as np

list(range(0, 10)) #Range from 0 to 10

arrRange = np.arange(0, 10) #Creates an Array of a range of numbers
arrRange2 = np.arange(0, 20, 2) #Creates an Array 2 by 2
print(f"Arrays with Range: {arrRange}\n2 by 2: {arrRange2}\n")

zeros = np.zeros((10, 10)) #Array made with only 0
print(f"{zeros}\n") #Used to make schemes of future Arrays

lineSpaces = np.linspace(0, 10, 100)
print(f"{lineSpaces}\n")

"""
Line Spaces:
Serves to go from a initial number to a final number in certain
values that we need, this serves to make a proporcional distribution
"""

diag = np.eye(4) #Create a Matrix with a diagonal with the number 1
print(f"{diag}")

randomArray = np.random.rand(4, 4) #Create the structure of a Matrix with random numbers
print(f"{randomArray}\n")

randomMatrix = np.random.randint(1, 100,(10, 10)) #Use random numbers to fill a defined prestructure
print(f"{randomMatrix}\n")