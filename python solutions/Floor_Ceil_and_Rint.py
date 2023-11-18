'''In this code, you set NumPy's print options to use a space as the sign character. 
Then, you read a list of numbers as input and create a NumPy array of floating-point numbers. 
You use NumPy functions to perform floor (round down), ceiling (round up), and rounding (round to the nearest integer) 
operations on the array. Finally, you print the results of each operation.'''

import numpy

# Set NumPy print options to use a space as the sign character.
numpy.set_printoptions(sign=' ')

# Read a space-separated list of numbers from the user as input and create a NumPy array of type float.
a = numpy.array(input().split(), float)

# Perform floor operation on the input array, which rounds down to the nearest integer.
print(numpy.floor(a))

# Perform ceiling operation on the input array, which rounds up to the nearest integer.
print(numpy.ceil(a))

# Perform rounding operation on the input array, which rounds to the nearest integer.
print(numpy.rint(a))
