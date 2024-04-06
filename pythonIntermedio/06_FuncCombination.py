#<<---Combinacion de funciones--->>#
def sum(x, y):
    sum = x + y
    return sum

def printResult(result):
    print(f"El resultado de la operacion es -> {result}")
    
printResult(sum(2, 5))

#<<---Funcion Lambda--->>#
resta = lambda x, y: x - y

printResta = lambda result: print(f"El resultado de la resta es -> {resta}")