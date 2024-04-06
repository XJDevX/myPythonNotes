#<<---Ejecutar archivos manualmente--->>#
file = open("./Example.py")

print(file.read()) #Leer todo un archivo

print(file.readline()) #Leer solo lineas indicadas

for line in file:
    print(line) #Combinable con bucles
    
file.close() #Cerrar archivo (Libera espacio en memoria RAM)
    
with open("./Example.py") as file: #No se necesita cerrar el archivo
    for line in file:
        print(line)