#<<---Apply Python's functions to the DFs--->>#
import pandas as pd

csvFile = pd.read_csv("./bestsellers.csv", sep=",", header=0)
csvFile2 = csvFile #Copy
print(f"DataFrame: \n{csvFile}\n\n")

#>> Function
def twoTimes(value):
    return value * 2

#>> Apply
csvFile2['Rating * 2'] = csvFile['User Rating'].apply(twoTimes) #Execute a functions to the values of the DF
print(f"Apply: \n{csvFile}\n")

csvFile2['Rating * 3'] = csvFile['User Rating'].apply(lambda x: x * 3) #Lambda function in the DF
print(f"Apply: \n{csvFile}\n")

#>> Apply with various columns or all the DF
csvFile['Rating * 3'] = csvFile.apply(lambda x: x['Year'] * 10 if x['Genre']=='Fiction' else x['Year'], axis=1)
print(f"Lambda with Condition: \n{csvFile}") #Lambda with condition in the axis 1 or columns