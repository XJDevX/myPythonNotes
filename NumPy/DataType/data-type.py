#<<---Datatypes with NumPy--->>#
import numpy as np

arr = np.array([0,1,2,3,4,5]) #Normal Array
print(arr.dtype) #Prints the datatype

arrFloat = np.array([0,1,2,3,4,5], dtype='float64') #Array changing the datatype
print(arr.dtype)
arr = arr.astype(np.float64) #Changes all datatypes to Float

arr = arr.astype(np.bool_) #Changes all datatypes to Booleans
arr = arr.astype(np.string_) #Changes all datatypes to Strings
arr = arr.astype(np.int8) #Changes all datatypes to Numbers

"""
The Array alwas has to have all the data in a same datatype,
this means that we can only have Booleans, Numbers, Strings,
Floats, etc. But the datatype can be only one.
"""