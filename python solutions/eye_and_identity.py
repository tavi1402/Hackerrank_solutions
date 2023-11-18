'''The code reads the matrix size, creates an identity matrix using NumPy's numpy.eye(), and then formats 
the output to align the ones and zeros for better readability. The result is printed as a formatted identity matrix.'''

import numpy  # Import the NumPy library for array operations

# Read the matrix size (number of rows and columns) from the user as input. It's expected as two space-separated integers.
size = tuple(map(int, input().split()))

# Create an identity matrix using NumPy's `numpy.eye()` function, where 'size' is unpacked into the function.
# An identity matrix is a square matrix with ones on the main diagonal and zeros elsewhere.
identity_matrix = numpy.eye(*size)

# Convert the identity matrix to a string and format the output:
# - Replace '1' with ' 1' to align the ones properly.
# - Replace '0' with ' 0' to align the zeros properly.
formatted_output = str(identity_matrix).replace('1', ' 1').replace('0', ' 0')

# Print the formatted identity matrix.
print(formatted_output)
