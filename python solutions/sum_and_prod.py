'''This code reads user input to create a 2D NumPy array and then performs two main operations:
It calculates the sum of elements along each column (vertical) of the array, resulting in an array of column sums.
It calculates the product of the elements in the array of column sums.
The final result is the product of the column sums. This code is effectively finding the product of the sums of each column in the 2D array.'''

import numpy

# Read two integers, N and M, from the user as input, representing the number of rows and columns.
N, M = map(int, input().split())

# Create a 2D NumPy array 'A' by reading 'N' lines of space-separated integers for 'M' columns.
A = numpy.array([input().split() for _ in range(N)], int)

# Calculate the sum of elements along the columns (axis=0), resulting in an array of column sums.
column_sums = numpy.sum(A, axis=0)

# Calculate the product of the elements in the array 'column_sums'.
result = numpy.prod(column_sums)

# Print the result, which is the product of the column sums.
print(result)
