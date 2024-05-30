#<<---Errors and how to manage them--->>#

#-> Manage own errors
age = 16

if age < 18:
    raise Exception("You're less than 18 years old, you can't enter")

#-> Manage errors from Python
try:
    print(0/0) #Zero Division Error
except ZeroDivisionError as error:
    print(error)