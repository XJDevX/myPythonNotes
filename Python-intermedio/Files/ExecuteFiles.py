#<<---Execute files manually--->>#
file = open("./Example.py")

print(file.read()) #Read all the file

print(file.readline()) #Read only the specified lines

for line in file:
    print(line) #Combinable with Loops
    
file.close() #Close the file (Frees RAM memory)
    
with open("./Example.py") as file: #It's not necesary to close the file
    for line in file:
        print(line)