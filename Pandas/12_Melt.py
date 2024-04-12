#<<---Melt--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n\n")

#>> Melt
csvFile2 = csvFile[['Name', 'Genre']].melt()
print(f"Melt: \n{csvFile2}\n")

"""
El método melt toma las columnas del DataFrame y las 
pasa a filas, con dos nuevas columnas para especificar 
la antigua columna y el valor que traía.
"""

csvFile3 = csvFile.melt(id_vars='Year', value_vars='Genre') #Organizar Año y Genero
print(f"Año y genero: \n{csvFile3}\n")