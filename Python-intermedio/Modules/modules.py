#<<---Modules--->>#
import sys #Knows the Operational System
import re #Searchs characters of a String
import time #Revisar tiempo local
import collections #Counts repeated data


print(sys.path) #Prints the Operational System

text = "My phone number is 321 123 12 34, the code of the country is +1"
result = re.findall("[0-9]+", text) #Searchs the numbers from 0 to 9
print(result)

timestamp = time.time()
local = time.localtime()
result = time.asctime() #Prints the real time
print(result)

numbers = [1,2,3,4,5,6,7,8,9,10]
counter = collections.Counter(numbers) #Counts numbers
print(counter)