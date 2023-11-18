'''In this code, the user is asked to input a shape (e.g., "2 3" for a 2x3 array), and then NumPy is used to 
create arrays of the specified shape filled with zeros and ones. The int data type is used to ensure that the 
array elements are integers. Finally, the arrays are printed with a newline character separating them.'''

import numpy as np  # Import the NumPy library for array operations

# Read the shape of the arrays from the user as input. The shape is a tuple of integers.
shape = tuple(map(int, input().split()))

# Create a NumPy array filled with zeros of the specified shape and data type 'int'.
zeros_array = np.zeros(shape, int)

# Create a NumPy array filled with ones of the specified shape and data type 'int'.
ones_array = np.ones(shape, int)

# Print the arrays with 'zeros' and 'ones' on separate lines, separated by a newline character.
print(zeros_array, ones_array, sep='\n')
