#<<---Agregando y eliminando datos con Pandas--->>#
import pandas as pd
import numpy as np

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
csvFile2 = csvFile
print(csvFile) #Abrir un archivo CSV con Pandas

#>> Eliminar filas y columnas
csvFile2 = csvFile2.drop('Genre', axis=1).head(11) #Borrando columnas
print(f"Eliminando columnas: \n{csvFile2}")

csvFile2 = csvFile2.drop(1, axis=0).head(2) #Borrando filas
print(f"Borrando filas: \n{csvFile2}")

#>> Agregar columnas
csvFile['Nueva Columna'] = np.nan
print(f"Agregando columnas: \n{csvFile}")

data = np.arange(0, csvFile.shape[0]) #Conseguir los valores de la primera columna
print(f"Numeros de la primera columna: \n{data}")

csvFile['Range'] = data #Crear una nueva columna con los valores de 'Data'
print(f"Agregando columnas desde rangos: \n{csvFile}") #Los rangos deben tener igual logitud

#>> Agregar columnas
csvFile = csvFile.add(csvFile) #Duplicar sus datos (No sus valores)
print(f"Duplicando valores: \n{csvFile}")