#<<---Options of the Strings--->>#
text = "This is an example"

#-> Options to modify the String
textLen = len(text) #-> Counts how many characters has the text.
textCount = text.count("A") #-> Counts how many times the String has the character defined.
textUpper = text.upper() #-> Converts the text to UPPERCASE.
textLower = text.lower() #-> Converts the text to lowercase.
textSwapCase = text.swapcase() #-> Inverts the characters order (A -> a).
textCapitalize = text.capitalize() #-> Puts the first letter in Uppercase.
textTitle = text.title() #-> Puts all the first letters in Uppercase.

#-> Options to make statements with Strings
textSW = text.startswith("Este") #-> Checks if it starts with the defined text.
textEW = text.endswith("Python") #-> Checks if it ends with the defined text.
textIsD = text.isdigit() #-> Checks if it's a single digit.
textReplace = text.replace("Example", "Program") #-> Replaces text.