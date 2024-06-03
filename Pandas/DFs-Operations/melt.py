#<<---Melt--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n\n")

#>> Melt
csvFile2 = csvFile[['Name', 'Genre']].melt()
print(f"Melt: \n{csvFile2}\n")

"""
The Melt method gets the columns of the DF and converts
them to rows, with two new columns to specificate the
old column and its value
"""

csvFile3 = csvFile.melt(id_vars='Year', value_vars='Genre') #Organize the Year and the Genre
print(f"Year and Genre: \n{csvFile3}\n")