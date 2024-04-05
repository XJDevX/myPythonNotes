#<<---Operaciones con Sets--->>#
mySetA = {1, 21.3, 3, "Hola", "Python", True}
mySetB = {3, "2.51", 10, "2024", "Python", False}

#-> Desde variables
union = mySetA.union(mySetB) #Unir dos Sets
intersec = mySetA.intersection(mySetB) #Intersecar datos en comun
diff = mySetA.difference(mySetB) #Buscar diferencias entre Sets
symDiff = mySetA.symmetric_difference(mySetB) #Diferencias simetricas

#-> Desde un "Print"
print(mySetA | mySetB) #Unir dos Sets
print(mySetA & mySetB) #Intersecar datos en comun
print(mySetA - mySetB) #Buscar diferencias
print(mySetA ^ mySetB) #Diferencias simetricas