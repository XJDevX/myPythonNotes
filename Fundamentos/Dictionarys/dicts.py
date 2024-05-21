#<<---Dictionarys--->>#
dict = {
    "Python": "Programming language",
    "Computador": "Tool for programming",
    "ChatGPT": "A nice friend in case of a doubt"
}

#-> Options of values in a Dictionary.
dict = dict.get("Python") # Obtains a value of the Dict.

dictChange = dict["ChatGPT"] = "Don't copy his code" # Replaces.

dictShowAll = print(dict.items()) # Prints all the items of the Dict.
dictShowKeys = print(dict.keys()) # Keys of the Dict.
dictShowValues = print(dict.values()) # Values of the Keys.