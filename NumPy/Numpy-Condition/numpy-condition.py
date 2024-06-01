#<<---Conditions with Numpy--->>#
import numpy as np

arr = np.linspace(1, 10, 10, dtype="int8")
print(f"Array: \n{arr}\n")

#-> Conditions
indCond = (arr > 5) & (arr < 9) #Numbers bigger than 5
print(f"{indCond}") #Print conditions with Arrays
arr2 = arr[indCond] #Search the values of the conditions in the original Array
print(f"{arr2}")

changeCond = arr[arr > 5] = 99
print(f"{arr}") #Change the values of an Array with conditions