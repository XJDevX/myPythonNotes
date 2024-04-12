#<<---Combinando DataFrames con Merge--->>#
import pandas as pd

dict1 = {
    'key': ['k0', 'k1', 'k2', 'k3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}

dict2 = {
    'key2': ['k0', 'k1', 'k2', 'k3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}

izq_df = pd.DataFrame(dict1) 
der_df = pd.DataFrame(dict2)
print(f"DataFrame1: \n{izq_df}\n\n")
print(f"DataFrame2: \n{der_df}\n\n")

print("*"*20,"Merge","*"*20,"\n") #Separador

#>> Merge
try:
    finalDF = izq_df.merge(der_df) #Merge por defecto si hay algo en comun
    print(f"Merge de los DFs: \n{finalDF}\n")
except:
    print(f"No se pueden hacer merge de DFs distintos!!!\n\n")

finalDF2 = izq_df.merge(der_df, left_on='key', right_on='key2') #Especificar columnas del merge (Si son diferentes)
print(f"Merge de los DFs especificando columnas: \n{finalDF2}\n") 

finalDF3 = izq_df.merge(der_df, left_on='key', right_on='key2', how='left') #Especificar el merge o union
print(f"Merge con forma en especifico: \n{finalDF3}\n")