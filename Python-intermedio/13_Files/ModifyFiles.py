#<<---Modificar archivos desde un archivo externo--->>#
with open("./Example.py", "r+") as file:
    for line in file:
        print(line)
    file.write("Modificacion externa de un archivo")