#<<---Operations with NumPy--->>#
import numpy as np

list = [1,2] #Normal list
print(f"List: {list}\nList * 2: {list * 2}\n") #Duplicate the values of the list

arr = np.arange(0, 10) #Array with Numpy
arr2 = arr.copy() #Copy the Array
print(f"Array: {arr}\nArray 2: {arr2}\n\n#<<---Operations--->>#")

#>> Operations with Arrays
print(f"Array ** 2: {arr2 ** 2}") #It can be make all operations
print(f"Sum of Arrays: {arr + arr2}")

#>> Operations with Matrixes
matrix = arr2.reshape(2, 5) #Reshape of the Matrix
matrix2 = matrix.copy()
print(f"\nMatrix: \n{matrix}\nMatrix 2: \n{matrix2}\n")
print(f"Matrix * Matrix2: \n{matrix * matrix2}")

print(f"\nPoint Product: \n{np.matmul(matrix, matrix2.T)}") #Point Product