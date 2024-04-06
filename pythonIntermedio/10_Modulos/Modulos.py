#<<---Modulos--->>#
import sys #Saber el sistema operativo
import re #Buscar caracteres en un String
import time #Revisar tiempo local
import collections #Contar datos repetidos


print(sys.path) #Imprimir sistema operativo

text = "Numero de celular es 321 123 12 34, el codigo del pais +1"
result = re.findall("[0-9]+", text) #Buscar numeros del 0 al 9
print(result)

timestamp = time.time()
local = time.localtime()
result = time.asctime()
print(result)

numbers = [1,2,3,4,5,6,7,8,9,10]
counter = collections.Counter(numbers) #Contar numeros
print(counter)