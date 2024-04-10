#<<---Como hacer un Array con NumPy--->>#
import numpy as np

lista = [1,2,3,4,6,7,8,9]
arr = np.array(lista) #Crear un array con NumPy

matriz = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(matriz) #Crear una Matriz con varias dimensiones

#-> Indexing
arr[0] + arr[5] #Operar datos de un Array
matriz[0, 2] + matriz[2, 1] #Operar datos de una matriz

"""
Al hacer Indexing con numpy y Matrices ponemos primero
el numero de la fila y luego el numero de columnas
    matriz[0, 2]
"""

#-> Slicing
arr[3:7] #Acceder a varios valores del Array
matriz[1:, 0:2] #Acceder a varios valores de la Matriz