#<<---Combine Functions--->>#
def sum(x, y):
    sum = x + y
    return sum

def printResult(result):
    print(f"The result of the operation is: {result}")
    
printResult(sum(2, 5))

#<<---Funcion Lambda--->>#
substract = lambda x, y: x - y

printSubstract = lambda result: print(f"The result of the substract is: {substract}")