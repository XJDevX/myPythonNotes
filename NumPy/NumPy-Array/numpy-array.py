#<<---How to make an Array with Numpy--->>#
import numpy as np

list = [1,2,3,4,6,7,8,9]
arr = np.array(list) #Creates an Array with Numpy
print(f"Array -> {arr}")

matrix = ([[1,2,3],[4,5,6],[7,8,9]])
mat = np.array(matrix) #Creates a Matrix with various dimensions
print(f"Matrix -> {mat}")

#-> Indexing
print(f"Sum the data of the Arrays -> {arr[0] + arr[5]}") #Operates data of an Array
print(f"Sum the data of the Matrices -> {mat[0, 2] + mat[2, 1]}") #Operates data of a Matrix


"""
When we make Indexing with Numpy and Matrices we
put first the number of the row and after that, the
number of the columns
    matrix[0,2]
"""

#-> Slicing
print(arr[3:7]) #Obtains various values of the Array
print(mat[1:, 0:2]) #Obtains various values of the Matrix