#<<---Shape and Reshape--->>#
import numpy as np

arr = np.random.randint(1, 10, (3,2))
print(f"Array: \n{arr}\nShape -> {arr.shape}\n") #See the Array's form

print(f"Reshape (1, 6):\n{np.reshape(arr, (1, 6), 'A')}") 

"""
When we use Reshape we can use the parameter that adjest
to the number of memory of our PC, this serves to avoid
certain errors with some devices.
It's used: "A" after the Reshape:

    np.reshape(arr, (1,6), "A")
    
It should be clarified that when we make the Reshape we
have to preserve the number of elements thath we had in
the beggining, this means that we can't add more numbers
that the ones we had.

    np.reshape(arr, (1, 6), "A") -> Yes
    np.reshape(arr, (10, 60), "A") -> No
    
"""