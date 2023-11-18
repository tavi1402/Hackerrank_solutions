'''This code takes two sets of inputs, creates NumPy arrays arr1 and arr2, and then concatenates them along the rows 
(axis 0) to form the final result. It's a common technique for stacking or combining arrays when working with NumPy.'''

import numpy as np  # Import the NumPy library for working with arrays

# Read integer values for 'a', 'b', and 'c' from user input
a, b, c = map(int, input().split())

# Create an array 'arr1' by reading 'a' lines of space-separated integers
arr1 = np.array([input().split() for _ in range(a)], int)

# Create another array 'arr2' by reading 'b' lines of space-separated integers
arr2 = np.array([input().split() for _ in range(b)], int)

# Concatenate 'arr1' and 'arr2' along the first axis (axis 0) to stack 'arr2' below 'arr1'
result = np.concatenate((arr1, arr2), axis = 0)

# Print the concatenated array
print(result)
