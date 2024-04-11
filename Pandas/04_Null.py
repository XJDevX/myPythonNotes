#<<---Valores nulos con Pandas--->>#
import pandas as pd
import numpy as np

dict = {
    'C1': [1,2,3,np.nan],
    'C2': [4,np.nan,6,7],
    'C3': ['A','B','C',None]        
}

df = pd.DataFrame(dict)
print(f"\nDataframe: \n{df}\n") #Crear un DataFrame


print(f"Dataframe is Null? (True or False): \n{df.isnull()}\n") #Utiliza True y False
print(f"Dataframe is Null? (0 or 1): \n{df.isnull()*1}\n") #Pero utilizar 1s y 0s es mas entendible
print(f"Missing data: \n{df.fillna('Missing')}\n") #Datos none = 'Missing' o cualquier otro dato

print(f"Interpolate: \n{df.interpolate()}\n") #Seguir una secuencia con los nulos (Numeros)
print(f"Eliminar nulos: \n{df.dropna()}\n") #Eliminar valores nulos