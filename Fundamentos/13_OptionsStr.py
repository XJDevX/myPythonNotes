#<<---Parametros de los Strings--->>#
text = "Este es un ejemplo"

#-> Parametros para modificar el String
textLen = len(text) #-> Cuantos caracteres tiene el texto
textCount = text.count("A") #-> Cuantas veces tiene el caracter indicado
textUpper = text.upper() #-> Pasar el texto a MAYUSCULAS
textLower = text.lower() #-> Pasar el texto a minusculas
textSwapCase = text.swapcase() #-> Invertir orden de caracteres (A -> a)
textCapitalize = text.capitalize() #-> Pone primera letra en Mayuscula
textTitle = text.title() #-> Todas las letras iniciales en Mayuscula

#-> Parametros para hacer condiciones con Strings
textSW = text.startswith("Este") #-> Ver si inicia con el texto indicado
textEW = text.endswith("Python") #-> Ver si termina con el texto indicado
textIsD = text.isdigit() #-> Verificar si es un solo digito
textReplace = text.replace("Ejemplo", "Programa") #-> Reemplazar texto