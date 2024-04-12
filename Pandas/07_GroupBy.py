#<<---Group By con Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n")

#>> GroupBy de columnas
author = csvFile.groupby('Author').count() #Author se convierte en el indice del DF
print(f"Autorhs: \n{author}\n") #.count() puede ser cualquier operacion estadistica

author = csvFile.groupby('Author').sum().loc['William Davis'] #Filtro con Loc
print(f"William Davis: \n{author}\n")

author = csvFile.groupby('Author').agg(['min', 'max']) #Minimo y Maximo (Funciones de '.agg')
print(f"Min and Max: \n{author}\n")

author = csvFile.groupby('Author').agg({'Reviews': ['min', 'max'],'User Rating':'mean'}) #Varias dunciones de '.agg'
print(f"Min and Max: \n{author}\n")

#>> Indices o llaves compuestas
authorAndYear = csvFile.groupby(['Author', 'Year']).count() #Varios indices o llaves
print(f"\n\nAutor y año: \n{authorAndYear}\n")