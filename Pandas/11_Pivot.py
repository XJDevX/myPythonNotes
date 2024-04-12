#<<---Pivot--->>#
import pandas as pd

csvFile = pd.read_csv("./02_bestsellers-with-categories.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n\n")

#>> Pivot Table
csvFile = csvFile.pivot_table(index='Genre',columns='Year',values='User Rating', aggfunc='sum')
print(csvFile) #Suma de genero a lo largo de los años

"""
Pivot sirve para hacer una nueva lista o DF con datos que
nosotros le indiquemos y se ajusten al resultado buscado, esto
se hace poniendo en el '.pivot_table()' los siguientes parametros

    * index='Genre' = Indice de filas
    * columns='Year' = Indice de columnas
    * values='User Rating' = Valores

    *(Opcional) aggfunc='sum' = Suma de valores del 'Values'

    (Puede ser cualquier valor del DF)
"""