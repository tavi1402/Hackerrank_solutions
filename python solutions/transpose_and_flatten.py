'''this code uses NumPy to manipulate a matrix. It reads the matrix from the user, converts it to a NumPy array, 
and then prints the transpose and flattened version of the array.'''

# Import the NumPy library.
import numpy

# Read integers n and m from the user.
n, m = map(int, input().split())

# Initialize an empty list 'ar' to store the matrix.
ar = []

# Read n rows of the matrix from the user.
for i in range(n):
    # Read a row, convert it to a list of integers, and append it to 'ar'.
    row = list(map(int, input().split()))
    ar.append(row)

# Create a NumPy array 'np_ar' from the list 'ar'.
np_ar = numpy.array(ar)

# Print the transpose of the NumPy array.
print(numpy.transpose(np_ar))

# Print the flattened version of the NumPy array.
print(np_ar.flatten())
