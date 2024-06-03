#<<---Principal functions with Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n")

#>> Principal functions
print(f"First 5 rows: \n{csvFile.head(5)}\n") #Print "N" initial rows
print(f"Last 5 rows: \n{csvFile.tail(5)}\n") #Print "N" last rows

print(f"\n{csvFile.info()}\n") #Column's info and its values

print(f"Stadistic values: \n{csvFile.describe()}\n") #Stadistic values are so usefull

print(f"Memory usage: \n{csvFile.memory_usage(deep=True)}") #See the Memory Usage of the values

print(f"\nAuthors' books: \n\n{csvFile['Author'].value_counts()}\n") #See the repetition of values in the columns

print(f"Deleting duplicated values: \n{csvFile.drop_duplicates()}\n") #Deleting duplicated values

print(f"Ascending values: \n{csvFile.sort_values('Year', ascending=True)}") #Order values by columns
print(f"Descending values: \n{csvFile.sort_values('Year', ascending=False)}") #Order values by columns