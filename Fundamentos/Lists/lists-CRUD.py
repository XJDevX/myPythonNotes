#<<---CRUD con listas--->>#
myList = [1, "Hello", False] # Create
myList2 = ["Hello", 2024, True] # Create

myList[-1] = True # Replace

myList.append("Python") # Adds a value at the end of the List.
myList.insert(1, True) # Adds a value in a specific position.
newList = myList + myList2 # Combine Lists.
newList.index("Python") # Searches values in the List.
newList.pop() # Deletes the last value of the List.
newList.reverse() # Inverts the order of the values.
newList.remove("Hola") # Deletes a value of the List.

numberList = [10,6,3,8,43,68,32]
numberList.sort() # Orders numbers smaller to larger numbers.