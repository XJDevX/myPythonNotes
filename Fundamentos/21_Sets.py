#<<---Sets--->>#
mySet = {1, 2.51, 3, "Hola", "Python", True} #No es tan modificable
myList = (1, 2.51, 3, "Hola", "Python", True) #Es mas modificable

#-> CRUD
lenght = len(mySet) #Longitud del Set
isIn = "Hola" in mySet #Comprobar un dato
add = mySet.add(19) #Agregar datos
update = mySet.update({"A", 2, 3}) #Agregar varios datos
remove = mySet.remove("Hola") #Eliminar datos y si no, genera error
discard = mySet.discard(1) #Eliminar datos y si no, no genera error
clear = mySet.clear() #Vaciar un Set