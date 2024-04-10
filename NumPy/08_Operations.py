#<<---Operaciones con NumPy--->>#
import numpy as np

lista = [1,2] #Lista normal
print(f"Lista: {lista}\nLista * 2: {lista * 2}\n") #Duplicar valores de la lista

arr = np.arange(0, 10) #Array con NumPy
arr2 = arr.copy() #Copiar el Array
print(f"Array: {arr}\nArray 2: {arr2}\n\n#<<---Operaciones--->>#")

#>> Operaciones con arrays
print(f"Array ** 2: {arr2 ** 2}") #Se puede con cualquier operacion
print(f"Suma de Arrays: {arr + arr2}")

#>> Operaciones con matrices
matriz = arr2.reshape(2, 5) #Reshape de Matriz
matriz2 = matriz.copy()
print(f"\nMatriz: \n{matriz}\nMatriz 2: \n{matriz2}\n")
print(f"Matriz * Matriz2: \n{matriz * matriz2}")

print(f"\nProducto punto: \n{np.matmul(matriz, matriz2.T)}") #Producto punto