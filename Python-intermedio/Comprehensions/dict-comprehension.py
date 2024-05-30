#<<---Dictionary Comprehension--->>#

#-> Normal Method
dictionary = {}
for number in range(1,11):
    dictionary[number] = number
    
#-> Comprehension Method
dictionary2 = {element: element for element in range(1,11)}

"""
Similar to the previous one, we have the Dictionary 
Comprehension, this one is realized with a parameter 
with an use called “Term-Meaning”
"""