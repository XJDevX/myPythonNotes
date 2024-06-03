#<<---Group By with Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n")

#>> GroupBy of Columns
author = csvFile.groupby('Author').count() #Author is converted to the index of the DF
print(f"Authors: \n{author}\n") #.count() could be any stadistic operation

author = csvFile.groupby('Author').sum().loc['William Davis'] #Filter with Loc
print(f"William Davis: \n{author}\n")

author = csvFile.groupby('Author').agg(['min', 'max']) #Min and Max (Functions of '.agg')
print(f"Min and Max: \n{author}\n")

author = csvFile.groupby('Author').agg({'Reviews': ['min', 'max'],'User Rating':'mean'}) #Various functions of '.agg'
print(f"Min and Max: \n{author}\n")

#>> Indexes or compuest keys
authorAndYear = csvFile.groupby(['Author', 'Year']).count() #Various Indexes or Keys
print(f"\n\nAuthor and Year: \n{authorAndYear}\n")