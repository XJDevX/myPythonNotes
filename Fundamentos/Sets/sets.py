#<<---Sets--->>#
mySet = {1, 2.51, 3, "Hello", "Python", True} # It's not so modifiable.
myList = (1, 2.51, 3, "Hello", "Python", True) # It's more modifiable. 

#-> CRUD
lenght = len(mySet) # Length of the Set.
isIn = "Hello" in mySet # Check if a value is in the Set.
add = mySet.add(19) # Adds values to the Set.
update = mySet.update({"A", 2, 3}) # Adds multiple values to the Set.
remove = mySet.remove("Hola") # Deletes values and if they aren't found, it returns an error.
discard = mySet.discard(1) # Deletes values and if they aren't found, it doesn't returns an error.
clear = mySet.clear() # Empties the Set.