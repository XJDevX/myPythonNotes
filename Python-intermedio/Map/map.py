#<<---Map()--->>#
numbers = [1,2,3,4,5]

numbersBy2 = list(map(lambda i: i * 2, numbers))

#-> Example
stock = [
    {
        "Product": "Shirt",
        "Price": 140
    },
    {
        "Product": "Jean",
        "Price": 100
    },
    {
        "Product": "Sweater",
        "Price": 235
    }
]

prices = list(map(lambda item: item["Precio"], stock))
products = list(map(lambda item: item["Producto"], stock))

"""
This method lets us add elements to a list like a Comprehension,
but with a Lambda function, including the parameters in the
same line. It should be clarified which is going to be the range
or the data to use.
"""