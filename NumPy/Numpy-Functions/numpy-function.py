#<<---Principal functions with Numpy--->>#
import numpy as np

arr = np.random.randint(1, 20, 10)
arr = arr.reshape(2, 5)
print(f"Array: \n{arr}\n")

#-> Most important functions
print(arr.max()) #Search the biggest number
print(f"{arr.max(0)}\n") #The biggest number by axis

print(f"{arr.argmax(0)}\n") #Search the index with the biggest number
#All the functions that work with "Max" also work with "Min"

print(f"{arr.ptp()}\n") #Difference between the smallest and the biggest number

print(f"{np.percentile(arr, 50)}\n") #Value of the middle or the operation of de middle values

print(f"{np.sort(arr)}\n") #Order the numbers from the smalles to the biggest

print(f"{np.median(arr)}\n") #Median of an Array

print(f"{np.std(arr)}") #Standard desviation of the Array

print(f"{np.var(arr)}") #Variance == Desviation ** 2

print(np.mean(arr)) #The half of the Array(Average)
a = np.array([[1,2,3],[4,5,6]])
b = np.array([7,8,9])

b = np.expand_dims(b, axis=0) #Expand dimensions to make them equal to the A's

c = np.concatenate((a, b), axis=0) #Join Arrays in one axis
print(f"{c}\n")

print(f"{b} -> {b.T}") #"T" Serves to change the order of the rows - columns