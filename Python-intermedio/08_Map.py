#<<---Map()--->>#
numbers = [1,2,3,4,5]

numbersBy2 = list(map(lambda i: i * 2, numbers))

#-> Ejemplo
stock = [
    {
        "Producto": "Camiseta",
        "Precio": 140
    },
    {
        "Producto": "Pantalon",
        "Precio": 100
    },
    {
        "Producto": "Saco",
        "Precio": 235
    }
]

prices = list(map(lambda item: item["Precio"], stock))
products = list(map(lambda item: item["Producto"], stock))

"""
Este método nos permite agregar elementos a una lista como si 
fuera un Comprehension, pero con una función lambda definiendo 
incluso los parámetros en la misma línea en la que se inicializa 
la variable. En esta se debe aclarar de donde sacaremos el rango 
o los datos a operar con la función Lambda.
"""