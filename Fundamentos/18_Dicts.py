#<<---Diccionarios--->>#
diccionario = {
    "Python": "Lenguaje de programacion",
    "Computador": "Herramienta para programar",
    "ChatGPT": "Buen compañero en caso de una duda"
}

#-> Opciones de datos en un Diccionario
diccPython = diccionario.get("Python") #Obtener un valor del diccionario

diccChange = diccionario["ChatGPT"] = "No copiarle codigo" #Reemplazar

diccShowAll = print(diccionario.items()) #Todos los items del diccionario
diccShowKeys = print(diccionario.keys()) #Terminos del diccionario
diccShowValues = print(diccionario.values()) #Valores de los terminos