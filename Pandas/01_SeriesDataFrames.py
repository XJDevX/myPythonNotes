#<<---Series y DataFrames con Pandas--->>#
import pandas as pd

#>> Series unidimensionales
players = pd.Series(["CR7", "Messi", "Mbappe", "Neymar"], index=[7, 10, 30, 25]) #Serie 1
print(f"Jugadores de futbol: \n{players}") #Son opcionales los indices

dicc = {7:"Ronaldo",10:"Messi",30:"Mbappe",25:"Neymar"} #Serie desde diccionario
players2 = pd.Series(dicc) #Si no hay indices se ponen por defecto
print(f"\n{players2}")

#>> Series bidimensionales
dict = {
    "Jugador":["CR7", "Messi", "Haaland"],      
    "Altura": ["183", "165", "189"],
    "Goles": ["845", "813", "524"]
}

playerStats = pd.DataFrame(dict)
print(f"\n\nDataFrame:\n{playerStats}\n")
print(f"Columnas: {playerStats.columns}\nIndex: {playerStats.index}")