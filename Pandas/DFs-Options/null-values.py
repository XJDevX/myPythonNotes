#<<---Null values with Pandas--->>#
import pandas as pd
import numpy as np

dict = {
    'C1': [1,2,3,np.nan],
    'C2': [4,np.nan,6,7],
    'C3': ['A','B','C',None]        
}

df = pd.DataFrame(dict)
print(f"\nDataframe: \n{df}\n") #CCreate a DF


print(f"Dataframe is Null? (True or False): \n{df.isnull()}\n") #Use True or False to know where the DF is null
print(f"Dataframe is Null? (0 or 1): \n{df.isnull()*1}\n") #But using 1s and 0s could be more readable
print(f"Missing data: \n{df.fillna('Missing')}\n") #Fill missing data: none = 'Missing' o any other value

print(f"Interpolate: \n{df.interpolate()}\n") #Follow a sequence with the null values (Numbers)
print(f"Delete nulls: \n{df.dropna()}\n") #Delete Null values