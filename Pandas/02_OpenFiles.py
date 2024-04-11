#<<---Abriendo archivos con Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
print(csvFile) #Abrir un archivo CSV con Pandas

jsonFile = pd.read_json("./02_hpcharactersdataraw.json", typ="Series")
print(jsonFile) #Abrir un archivo JSON con Pandas


#>> Filtrando los DataFrames importados especificos
print("\n\n","-#" * 10, "Filtrando DataFrames", "#-" * 10) #Separador

print(f"Primeras 4 filas: \n{csvFile[0:4]}") #Indexing
print(f"Categorias del DataFrame: \n{csvFile[['Name', 'Author']]}") #Nombre y autor

print(f"Por filas: \n{csvFile.loc[0:4, ['Name', 'Author']]}") #Slicing avanzado
print(f"Autor: \n{csvFile.loc[:, ['Author']] == 'JJ Smith'}")


#>> Filtrando los DataFrames por indices
print(f"Filtrado por indices: \n{csvFile.iloc[:, 0:3]}") #Similar a Loc