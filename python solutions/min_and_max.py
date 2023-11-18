'''this code takes input to create a 2D array, calculates the minimum value along each row, and then finds the 
maximum among those minimum values. The result is the maximum of the minimum values along each row in the 2D array.'''

import numpy as np  # Import the NumPy library for array operations

# Read two integers, N and M, from the user as input, representing the number of rows and columns.
N, M = map(int, input().split())

# Create a 2D NumPy array by reading N lines of space-separated integers for M columns.
# The array contains user-provided values.
data = np.array([input().split() for _ in range(N)], int)

# Calculate the minimum value along each row (axis=1) using `.min(1)`.
# This results in an array of minimum values for each row.
min_values_per_row = data.min(1)

# Find the maximum value among the minimum values using `.max()`.
# This provides the maximum value among the minimum values from all rows.
result = min_values_per_row.max()

# Print the maximum of the minimum values along each row.
print(result)
