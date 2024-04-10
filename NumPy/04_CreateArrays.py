#<<---Creando Arrays con NumPy--->>#
import numpy as np

list(range(0, 10)) #Rango de 0 a 10

arrRange = np.arange(0, 10) #Crear un array de un rango de numeros
arrRange2 = np.arange(0, 20, 2) #Crear un array de 2 en 2
print(f"Arrays con rango -> {arrRange}\nDe 2 en 2 -> {arrRange2}\n")

zeros = np.zeros((10, 10)) #Array compuesto por 0s
print(f"{zeros}\n") #Utilizado para hacer esquemas de futuros arrays

lineSpaces = np.linspace(0, 10, 100)
print(f"{lineSpaces}\n")

"""
#<Line Spaces>#
Sirver parra llegar de un numero inicial a un numero final en cierta
cantidad de valores que necesitemos, este sirve para hacer una distribucion
proporcional
"""

diag = np.eye(4) #Crear una matriz con diagonal 1
print(f"{diag}")

randomArray = np.random.rand(4, 4) #Estructura de matriz con numeros aleatorios
print(f"{randomArray}\n")

randomMatriz = np.random.randint(1, 100,(10, 10)) #N. aleatorios con estructura predefinida
print(f"{randomMatriz}\n")