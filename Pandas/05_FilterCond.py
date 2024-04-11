#<<---Filtrado por condiciones con Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
print(csvFile)

#>> Condiciones
mayorA2016 = csvFile['Year'] > 2016
print(f"Datos mayores a 2016: \n{csvFile[mayorA2016]}") #Filtros por condiciones

genreFiction = csvFile['Genre'] == 'Fiction'
print(f"Genero ficcion: \n{csvFile[genreFiction]}") #Filtrado por condicion

#>> Combinar condiciones
bestBooks = csvFile[mayorA2016 & genreFiction] #Combinar condiciones
print(f"Mejores libros: \n{bestBooks}\n")

print(f"Datos menores a 2016: \n{csvFile[-mayorA2016]}\n") #Hacer condiciones opuestas con '-'