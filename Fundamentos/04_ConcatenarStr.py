#<<---Concatenar Strings--->>#
suma = 10 + 9

#-> Metodo 1 (Mejor opcion)
print(f'Hola, "10 + 9" es {suma}!') #-> Se pone (f'') y entre corchetes los valores

#-> Metodo 2
print('Hola, "10 + 9" es ' + suma + '!')  #-> Se separan valores por '+'

#-> Metodo 3 (No recomendable)
print('Hola, "10 + 9" es {}!'.format(suma))  #-> Se ponen valores al final