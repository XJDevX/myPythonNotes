#<<---Filtering by Conditions in Pandas--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
print(csvFile)

#>> Conditions
biggerThan2016 = csvFile['Year'] > 2016
print(f"Values bigger than 2016: \n{csvFile[biggerThan2016]}") #Filtering by conditions

genre_Fiction = csvFile['Genre'] == 'Fiction'
print(f"Fictions genre: \n{csvFile[genre_Fiction]}") #Filtering by conditions

#>> Combine conditions
bestBooks = csvFile[biggerThan2016 & genre_Fiction] #Combining
print(f"Best books: \n{bestBooks}\n")

print(f"Values smaller than 2016: \n{csvFile[-biggerThan2016]}\n") #Make oposite conditions with '-'