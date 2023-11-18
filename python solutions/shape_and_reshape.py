''' this code showcases how to use NumPy to reshape a one-dimensional array of integers into a 3x3 matrix using the 
numpy.reshape function. The resulting matrix is then printed.'''

# Import the NumPy library.
import numpy

# Read a space-separated list of integers from the user, convert it to a list 'ar'.
ar = list(map(int, input().split()))

# Create a NumPy array 'np_ar' from the list 'ar'.
np_ar = numpy.array(ar)

# Reshape the NumPy array into a 3x3 matrix and print the result.
print(numpy.reshape(np_ar, (3, 3)))
