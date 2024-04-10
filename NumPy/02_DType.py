#<<---Tipos de datos con NumPy--->>#
import numpy as np

arr = np.array([0,1,2,3,4,5]) #Array Normal
print(arr.dtype) #Imprimir tipos de datos

arrFloat = np.array([0,1,2,3,4,5], dtype='float64') #Array cambiando el tipo de dato
print(arr.dtype) #Imprimir tipos de datos
arr = arr.astype(np.float64) #Cambiar tipo de datos a Float

arr = arr.astype(np.bool_) #Cambiar tipo de datos a Booleanos
arr = arr.astype(np.string_) #Cambiar tipo de datos a String
arr = arr.astype(np.int8) #Cambiar tipo de datos a Numeros

"""
El Array siempre debe tener todos los datos de un mismo valor,
esto significa que solo podemos tener Booleanos, Numeros, Strings
Floats, etc. Pero solo debe ser uno
"""