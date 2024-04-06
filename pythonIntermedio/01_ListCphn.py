#<<---List Comprehension--->>#

#-> Metodo normal
numbers = []
for number in range(1,11):
    numbers.append(numbers)
    
#-> Metodo Comprehension
numbers2 = [number for number in range(1,11)]

"""
Lo que hacemos con este código es añadir números 
del 1 al 10 con un “For”, esto se puede simplificar 
poniendo el método Comprehension, cabe aclarar que 
en este método el primer “number” en los “[]” es el 
que se agregara a la lista y el segundo “number” es el 
iterable en el bucle “For”.
"""