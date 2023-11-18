'''this code reads user input to create two 2D NumPy arrays, 'a' and 'b', and then calculates their dot product 
using np.dot(). The dot product is a mathematical operation that combines two arrays to produce a single scalar 
value or array, depending on the arrays' dimensions.'''

import numpy as np  # Import the NumPy library for array operations

# Read an integer 'n' from the user as input, representing the number of rows and columns in the arrays.
n = int(input())

# Create a 2D NumPy array 'a' by reading 'n' lines of space-separated integers for each row. The array contains user-provided values.
a = np.array([input().split() for _ in range(n)], int)

# Create another 2D NumPy array 'b' in a similar way, with the same number of rows and columns.
b = np.array([input().split() for _ in range(n)], int)

# Calculate and print the dot product of the two arrays 'a' and 'b' using `np.dot(a, b)`.
dot_product = np.dot(a, b)

# Print the result, which is the dot product of the arrays.
print(dot_product)
