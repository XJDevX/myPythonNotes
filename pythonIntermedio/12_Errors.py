#<<---Manejos de errores--->>#

#-> Manejo de errores propios
age = 16

if age < 18:
    raise Exception("Eres menor de edad, no puedes entrar")

#-> Manejo de errores de Python
try:
    print(0/0) #Error de division por 0
except ZeroDivisionError as error:
    print(error)