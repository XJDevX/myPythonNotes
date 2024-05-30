#<<---Dimensions--->>#
import numpy as np

scalar = np.array(42) #Zero Dimensions
print(f"{scalar}, Dimensions: {scalar.ndim}\n")

vector = np.array([1,2,3]) #One Dimension
print(f"{vector}, Dimensions: {vector.ndim}\n")

matrix = np.array([[1,2,3],[4,5,6]]) #Two Dimensions
print(f"{matrix}, Dimensions: {matrix.ndim}\n")

tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]]]) #Undefined dimensions, we put how many of those will be
print(f"{tensor}, Dimensions: {tensor.ndim}\n")

#<<---Add or Delete dimensions--->>#
exampleArray = np.array([1,2,3], ndmin=10) #Put a certain value of dimensions
print(f"{exampleArray}, Dimensions: {exampleArray.ndim}\n")

expand = np.expand_dims(np.array([1,2,3]), axis=0) #Expand one dimension
print(f"{expand}, Dimensions: {expand.ndim}\n")

print(f"{exampleArray}, Dimensions: {exampleArray.ndim}\n") 
exampleArray2 = np.squeeze(exampleArray) #Adjust the used dimensions
print(f"{exampleArray2}, Dimensions: {exampleArray2.ndim}\n") 
