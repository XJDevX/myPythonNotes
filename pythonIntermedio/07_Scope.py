#<<--Scope o alcanze de funciones--->>#
exampleGlobal = "Example"

def exampleFunc():
    exampleLocal = "Example"
    
"""
El Scope es el rango de las variables dentro de un programa, esto 
se debe a que a veces queremos llamar variables que se inicializaron 
en una función y no se puede, esto pasa porque la variable se define 
con un Scope local, lo que significa que solo existe dentro de la 
función, en cambio, cuando declaramos una variable por fuera de una 
función, esta se inicializara como una variable de Scope global que 
significa que esta variable se puede utilizar en todo el programa 
sin ningún error de alcance.
"""