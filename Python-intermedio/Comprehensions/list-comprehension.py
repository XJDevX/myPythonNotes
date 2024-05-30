#<<---List Comprehension--->>#

#-> Normal Method
numbers = []
for number in range(1,11):
    numbers.append(numbers)
    
#-> Comprehension Method
numbers2 = [number for number in range(1,11)]

"""
Here we are adding numbers from 1 to 10 with 
a loop 'For', we can simplify using the Comprehension 
Method. It should be clarified that in this method the 
first 'number' in the '[]' is the value that will be 
aggregated to the list and the second 'number' is the 
iterable in the loop 'For'.
"""