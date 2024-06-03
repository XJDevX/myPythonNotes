#<<---Pivot--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
print(f"DataFrame: \n{csvFile}\n\n")

#>> Pivot Table
csvFile = csvFile.pivot_table(index='Genre',columns='Year',values='User Rating', aggfunc='sum')
print(csvFile) #Sum the genre along the years

"""
Pivot serves to make a new list or DF with the values that
we want, this can be made by putting in the '.pivot_table()'
the following parameters:

    * index='Genre' -> Index of the Rows
    * columns='Year -> Index of the Columns
    * values='User Rating' = Values
    
    * (Optional) aggfunc='sum' -> Sum of the data of 'Values'
"""