#<<---Funciones principales con NumPy--->>#
import numpy as np

arr = np.random.randint(1, 20, 10)
arr = arr.reshape(2, 5)
print(f"Array: \n{arr}\n")

#-> Funciones mas importantes
print(arr.max()) #Buscar el numero mas grande
print(f"{arr.max(0)}\n") #Numero mayor por ejes

print(f"{arr.argmax(0)}\n") #Buscar el indice con el numero mayor
#Todas las funciones con "Max" tambien funcionan con "Min"

print(f"{arr.ptp()}\n") #Diferencia entre el numero mas pequeño y mas grande

print(f"{np.percentile(arr, 50)}\n") #Valor de la mitad o la operacion de valores en la mitad

print(f"{np.sort(arr)}\n") #Ordenar de menor a mayor los numeros

print(f"{np.median(arr)}\n") #Mediana de un arreglo

print(f"{np.std(arr)}") #Desviacion estandar del array

print(f"{np.var(arr)}") #Variancia == Desviacion ** 2

print(np.mean(arr)) #Media del array (Promedio)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([7,8,9])

b = np.expand_dims(b, axis=0) #Expandir dimensiones para que sean iguales a las de "A"

c = np.concatenate((a, b), axis=0)
print(f"{c}\n")

print(f"{b} -> {b.T}") #"T" Sirve para cambiar el orden de filas - columnas