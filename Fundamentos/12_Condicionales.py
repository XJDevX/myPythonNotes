#<<---Condicionales--->>#
precio = 20
presupuesto = int(input("Cuantos dolares tienes? -> "))

if presupuesto >= precio: #-> Puedo comprar el producto
    print("Compro el producto")
elif presupuesto <= precio - precio / 4: #-> Me falta poco para comprarlo
    print("Busco rebaja del producto")
else: #-> No compro el producto porque no tengo dinero
    print("No lo compro")    
    
"""
“If”, Comprueba si las condiciones dadas se cumplen o no.
“Elif”, Si la anterior condición no se cumplió comprueba con esta.
“Else”, Si ninguna de las condiciones se cumplió llega a una conclusión 
  definitiva que nosotros le especifiquemos en el código.
"""