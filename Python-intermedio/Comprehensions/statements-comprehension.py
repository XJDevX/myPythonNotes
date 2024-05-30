#<<---Comprehension with statementsComprehension con condiciones--->>#
import random #Numeros aleatorios

persons = ["Samuel", "Kevin", "David", "Julian", "Nicolas"]
personsAge = {person: random.randint(1, 40) for person in persons}

accepted = {person: age for (person, age) in personsAge.items() if age >= 18}
denied = {person: age for (person, age) in personsAge.items() if age < 18}

"""
In this example we can see that every person has a 
random age, with this we iter the dictionary "personsAge" 
to obtain the age for every person. After that, with the 
variables "accepted" and "denied" we verify the age to know 
if it's greater than 18 years old.
"""