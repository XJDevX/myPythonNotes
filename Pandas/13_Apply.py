#<<---Apply (Aplicar funciones de Python a los DFs)--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
csvFile2 = csvFile #Copia
print(f"DataFrame: \n{csvFile}\n\n")

#>> Funcion
def twoTimes(value):
    return value * 2

#>> Apply
csvFile2['Rating * 2'] = csvFile['User Rating'].apply(twoTimes) #Ejecutar una funcion a los valores del DF
print(f"Apply: \n{csvFile}\n")

csvFile2['Rating * 3'] = csvFile['User Rating'].apply(lambda x: x * 3) #Lambda function en el DF
print(f"Apply: \n{csvFile}\n")

#>> Apply con varias columnas o todo el DF
csvFile['Rating * 3'] = csvFile.apply(lambda x: x['Year'] * 10 if x['Genre']=='Fiction' else x['Year'], axis=1)
print(f"Lambda con condicion: \n{csvFile}") #Lambda con condicion en el axis 1 o columnas