#<<---Opening files with Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
print(csvFile) #Open a CSV file with Pandas

jsonFile = pd.read_json("./hpcharactersdataraw.json", typ="Series")
print(jsonFile) #Open a JSON file with Pandas


#>> Filtering DataFrames
print("\n\n","-#" * 10, "Filtrando DataFrames", "#-" * 10)

print(f"First 4 rows: \n{csvFile[0:4]}") #Indexing
print(f"Categories of the DataFrame: \n{csvFile[['Name', 'Author']]}") #Name and Author

print(f"PBy rows: \n{csvFile.loc[0:4, ['Name', 'Author']]}") #Advanced Slicing
print(f"Author: \n{csvFile.loc[:, ['Author']] == 'JJ Smith'}")


#>> Filtering the DFs by Indexes
print(f"Filter by indexes: \n{csvFile.iloc[:, 0:3]}") #Similar to Loc