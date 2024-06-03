#<<---Series and DataFrames with Pandas--->>#
import pandas as pd

#>> Unidimensional Series
players = pd.Series(["CR7", "Messi", "Mbappe", "Neymar"], index=[7, 10, 30, 25]) #First Serie
print(f"Soccer Players: \n{players}") #The indexes are optional

dicc = {7:"Ronaldo",10:"Messi",30:"Mbappe",25:"Neymar"} #Serie from a Dictionary
players2 = pd.Series(dicc) #If there are no indexes, they'll be asigned by default
print(f"\n{players2}")

#>> Bidimensional Series
dict = {
    "Player":["CR7", "Messi", "Haaland"],      
    "Height": ["183", "165", "189"],
    "Goals": ["845", "813", "524"]
}

playerStats = pd.DataFrame(dict)
print(f"\n\nDataFrame:\n{playerStats}\n")
print(f"Columns: {playerStats.columns}\nIndex: {playerStats.index}")