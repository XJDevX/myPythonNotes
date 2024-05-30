#<<---Modify files from external files--->>#
with open("./Example.py", "r+") as file:
    for line in file:
        print(line)
    file.write("Modifying files from external files")