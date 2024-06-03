#<<---Adding and deleting data with Pandas--->>#
import pandas as pd
import numpy as np

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
csvFile2 = csvFile
print(csvFile) #Open a CSV file with Pandas

#>> Delete Rows and Columns
csvFile2 = csvFile2.drop('Genre', axis=1).head(11) #Deleting Columns
print(f"Deleting columns: \n{csvFile2}")

csvFile2 = csvFile2.drop(1, axis=0).head(2) #Deleting Rows
print(f"Deleting row: \n{csvFile2}")

#>> Adding columns
csvFile['New Column'] = np.nan
print(f"Adding columns: \n{csvFile}")

data = np.arange(0, csvFile.shape[0]) #Get the values of a specific column
print(f"Numbers of the First Column: \n{data}")

csvFile['Range'] = data #Create a new column with the values of 'Data'
print(f"Adding Columns by Ranges \n{csvFile}") #The ranges have to have the same lenght

#>> Duplicate Values to Columns
csvFile = csvFile.add(csvFile) #Duplicate their data (Not their values)
print(f"Duplicating values: \n{csvFile}")