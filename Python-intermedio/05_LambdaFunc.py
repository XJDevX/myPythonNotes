#<<---Funciones Lambda--->>#

#<<---Funcion normal--->>#
def funcionNormal(x, y):
    result = x + y
    return result

#<<---Funcion Lambda--->>#
lambdaFunc = lambda x, y: x + y

"""
En este ejemplo vemos que las funciones Lambda llegan al mismo 
resultado que una función simple, la función Lambda recibe los 
parámetros de entrada antes de los “:”, después de estos se 
ponen los datos a operar para que la función retorne cierto valor, 
estas funciones solo se pueden definir junto a una variable, 
ya que, sin esta no habría a quien asignarle el 
valor de la función Lambda.
"""