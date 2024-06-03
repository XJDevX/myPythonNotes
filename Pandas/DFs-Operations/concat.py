#<<---Joining DFs with Concat--->>#
import pandas as pd

dict1 = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']    
}

dict2 = {
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']    
}

df1 = pd.DataFrame(dict1) #DataFrame 1
df2 = pd.DataFrame(dict2) #DataFrame 2
print(f"\nDataFrame1: \n{df1}\n\n")
print(f"DataFrame2: \n{df2}\n\n")


print("*"*20,"Concat","*"*20,"\n")


#>> Concat
df3 = pd.concat([df1, df2], ignore_index=True) #Join DFs and ignore the indexes by rows
print(f"Concat DataFrames (Axis 0): \n{df3}\n") #It's joined by default in the axis 0 (Rows)

df3 = pd.concat([df1, df2], axis=1) #Join DFs and ignore the indexes by columns
print(f"Concat DataFrames (Axis 1): \n{df3}\n\n") #It's joined in the axis 1 (Columns)
