#<<---Funciones principales de Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n")

#>> Funciones principales
print(f"Primeras 5 lineas: \n{csvFile.head(5)}\n") #Imprimir "N" cantidad de lineas iniciales
print(f"Ultimas 5 lineas: \n{csvFile.tail(5)}\n") #Imprimir "N" cantidad de lineas finales

print(f"\n{csvFile.info()}\n") #Informacion de columnas y sus valores

print(f"Valores estadisticos: \n{csvFile.describe()}\n") #Valores estadisticos bastante utiles

print(f"Uso de memoria: \n{csvFile.memory_usage(deep=True)}") #Ver el uso de memoria de los datos

print(f"\nLibros de autores: \n\n{csvFile['Author'].value_counts()}\n") #Ver la repeticion de datos de columnas

print(f"Eliminar duplicados: \n{csvFile.drop_duplicates()}\n") #Eliminar datos duplicados

print(f"Valores ascendientes: \n{csvFile.sort_values('Year', ascending=True)}") #Ordenar datos por columnas
print(f"Valores descendientes: \n{csvFile.sort_values('Year', ascending=False)}") #Ordenar datos por columnas