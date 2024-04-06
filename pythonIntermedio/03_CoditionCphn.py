#<<---Comprehension con condiciones--->>#
import random #Numeros aleatorios

persons = ["Samuel", "Kevin", "David", "Julian", "Nicolas"]
personsAge = {person: random.randint(1, 40) for person in persons}

accepted = {person: age for (person, age) in personsAge.items() if age >= 18}
denied = {person: age for (person, age) in personsAge.items() if age < 18}

"""
En este ejemplo vemos como es que le ponemos una edad
aleatoria a cada uno de los valores de nuestra lista “persons”, 
luego iteramos el diccionario “personsAge” para obtener la edad 
asignada para cada persona, luego con las variables “accepted” 
y “denied” verificamos la edad de los individuos para saber si 
tienen más de 18 años. En el siguiente ejemplo vemos como quedaría 
este código en el resultado final del programa, podemos observar que 
los datos si son agregados aleatoriamente.
"""