'''the code reads user input to create a 2D array and then calculates and prints the mean values along each row, 
the variance values along each column, and the overall standard deviation of the entire array. 
Each set of results is printed on a new line.'''

import numpy as np  # Import the NumPy library for array operations

# Read two integers, 'n' and 'm', from the user as input, representing the number of rows and columns.
n, m = map(int, input().split())

# Create a 2D NumPy array 'k' by reading 'n' lines of space-separated integers for 'm' columns. The array contains user-provided values.
k = np.array([input().split() for _ in range(n)], dtype=int)

# Calculate the mean along each row (axis=1) using `np.mean(k, axis=1)`. This results in an array of mean values for each row.
mean_per_row = np.mean(k, axis=1)

# Calculate the variance along columns (axis=0) using `np.var(k, axis=0)`. This results in an array of variance values for each column.
variance_per_column = np.var(k, axis=0)

# Calculate the overall standard deviation of the entire array using `np.std(k)`.
std_overall = np.std(k)

# Print the results of mean, variance, and standard deviation, separated by a newline character.
print(mean_per_row, variance_per_column, std_overall, '\n')
