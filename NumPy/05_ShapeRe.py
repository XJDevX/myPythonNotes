#<<---Shape and Reshape--->>#
import numpy as np

arr = np.random.randint(1, 10, (3,2))
print(f"Array: \n{arr}\nShape -> {arr.shape}\n") #Ver la forma del Array

print(f"Reshape (1, 6):\n{np.reshape(arr, (1, 6), "A")}") 

"""
Al momento de utilizar Reshape podemos utilizar el parametro
que lo ajusta a la cantidad de memoria de nuestro computador,
esto para evitar errores con dispositivos en especifico.
Se utiliza: "A" despues del Reshape: 

    np.reshape(arr, (1, 6), "A")
    
Cabe aclarar que al hacer el Reshape debemos conservar la
cantidad de elementos que teniamos al inicio, esto significa
que no podemos añadir mas numeros de los que teniamos:

    np.reshape(arr, (1, 6), "A") -> Si
    np.reshape(arr, (10, 60), "A") -> No
    
"""