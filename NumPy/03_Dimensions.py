#<<---Dimensiones--->>#
import numpy as np

scalar = np.array(42) #0 Dimensiones
print(f"{scalar}, Dimensiones: {scalar.ndim}\n")

vector = np.array([1,2,3]) #1 Dimension
print(f"{vector}, Dimensiones: {vector.ndim}\n")

matriz = np.array([[1,2,3],[4,5,6]]) #2 Dimensiones
print(f"{matriz}, Dimensiones: {matriz.ndim}\n")

tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]]])
print(f"{tensor}, Dimensiones: {tensor.ndim}\n")

#<<---Agregar o eliminar dimensiones--->>#
exampleArray = np.array([1,2,3], ndmin=10) #Poner cierta cantidad de dimensiones
print(f"{exampleArray}, Dimensiones: {exampleArray.ndim}\n")

expand = np.expand_dims(np.array([1,2,3]), axis=0) #Expandir una dimension
print(f"{expand}, Dimensiones: {expand.ndim}\n")

print(f"{exampleArray}, Dimensiones: {exampleArray.ndim}\n") 
exampleArray2 = np.squeeze(exampleArray) #Ajustar a las dimensiones usadas
print(f"{exampleArray2}, Dimensiones: {exampleArray2.ndim}\n") 
