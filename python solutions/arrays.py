'''This code defines a function arrays that takes a list of space-separated values as input, converts it into a NumPy 
array with reversed elements, and converts the elements to floating-point numbers. It then reads a space-separated 
string of values from the user, applies the arrays function to it, and prints the resulting NumPy array.'''

# Import the NumPy library.
import numpy

# Define a function 'arrays' that takes a list 'arr' as input and returns a reversed NumPy array of float values.
def arrays(arr):
    return numpy.array(arr[::-1], float)

# Read a space-separated string of values from the user, split it into a list 'arr'.
arr = input().strip().split(' ')

# Call the 'arrays' function with the list 'arr' and store the result in 'result'.
result = arrays(arr)

# Print the resulting NumPy array.
print(result)
