#<<---Dictionary Comprehension--->>#

#-> Metodo normal
dictionary = {}
for number in range(1,11):
    dictionary[number] = number
    
#-> Metodo Comprehension
dictionary2 = {element: element for element in range(1,11)}

"""
Similar al anterior tenemos el Dictionary Comprehension, 
este se realiza con un parámetro más debido 
a su uso “Termino -Significado”
"""