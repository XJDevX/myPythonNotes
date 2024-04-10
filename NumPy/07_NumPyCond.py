#<<---Condiciones con NumPy--->>#
import numpy as np

arr = np.linspace(1, 10, 10, dtype="int8")
print(f"Array: \n{arr}\n")

#-> Condiciones
indCond = (arr > 5) & (arr < 9) #Numeros mayores a 5
print(f"{indCond}") #Imprimir condiciones con Arrays
arr2 = arr[indCond] #Buscar los datos de las condiciones en el array original
print(f"{arr2}")

changeCond = arr[arr > 5] = 99
print(f"{arr}") #Cambiar datos de array con condiciones