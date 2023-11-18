'''This code uses NumPy to calculate the determinant of a square matrix. '''

import numpy as np  # Import the NumPy library for array operations

# Set NumPy print options to use legacy formatting with floating-point precision of '1.13'.
np.set_printoptions(legacy='1.13')

# Read an integer 'n' from the user as input, which represents the number of rows and columns in the square matrix.
n = int(input())

# Create a 2D NumPy array 'array' by reading 'n' lines of space-separated floating-point numbers for each row. The array contains user-provided values.
array = np.array([input().split() for _ in range(n)], float)

# Calculate and print the determinant of the square matrix using `np.linalg.det(array)`.
determinant = np.linalg.det(array)

# Print the determinant of the matrix.
print(determinant)
