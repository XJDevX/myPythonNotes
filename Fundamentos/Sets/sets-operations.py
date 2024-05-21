#<<---Operations with Sets--->>#
mySetA = {1, 21.3, 3, "Hello", "Python", True}
mySetB = {3, "2.51", 10, "2024", "Python", False}

#-> Desde variables
union = mySetA.union(mySetB) # Joins two Sets.
intersection = mySetA.intersection(mySetB) # Intersects common values.
diff = mySetA.difference(mySetB) # Searches diferences between the Sets.
symDiff = mySetA.symmetric_difference(mySetB) # Shows the Symmetric Differences.

#-> From a "Print"
print(mySetA | mySetB) # Joins two Sets.
print(mySetA & mySetB) # Intersects common values.
print(mySetA - mySetB) # Searches diferences between the Sets.
print(mySetA ^ mySetB) # Shows the Symmetric Differences.