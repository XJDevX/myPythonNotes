#<<---Joining DataFrames with Join--->>#
import pandas as pd

izq_df = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['k0', 'k1', 'k2']) #Indexes

der_df = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']}, 
    index=['k0', 'k2', 'k3'] #Indexes
) 

print(f"DataFrame1: \n{izq_df}\n\n")
print(f"DataFrame2: \n{der_df}\n\n")

print("*"*20,"Join","*"*20,"\n")

#>> Join (Index Match)
finalDF = izq_df.join(der_df, how='inner') #Join with the Indexes (Inner)
print(f"Join DFs: \n{finalDF}\n")

finalDF2 = izq_df.join(der_df, how='outer') #Join with the Indexes (Outer)
print(f"Join DFs (Outer): \n{finalDF2}\n")