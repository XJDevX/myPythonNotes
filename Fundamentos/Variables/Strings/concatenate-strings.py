#<<---Concatenate Strings--->>#
sum = 10 + 9

#-> First Method (Best Option)
print(f'Hi, "10 + 9" is {sum}!') #-> We put f('') and in brackets we put the variables or values

#-> Second Method
print('Hi, "10 + 9" is ' + sum + '!')  #-> We separate the values with a '+'

#-> Third Method (Not recommended)
print('Hi, "10 + 9" is {}!'.format(sum))  #-> We put the values at the end