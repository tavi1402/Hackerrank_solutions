'''This code uses NumPy to perform two operations, the inner product and the outer product, on two NumPy arrays 
'A' and 'B'.'''

import numpy as np  # Import the NumPy library for array operations

# Read space-separated integers from the user as input and create NumPy arrays 'A' and 'B'.
A = np.array(input().split(), int)
B = np.array(input().split(), int)

# Calculate and print the inner product of the two arrays 'A' and 'B' using `np.inner(A, B)`.
inner_product = np.inner(A, B)

# Calculate and print the outer product of the two arrays 'A' and 'B' using `np.outer(A, B)`.
outer_product = np.outer(A, B)

# Print the results of the inner and outer products, separated by newline characters.
print(inner_product, outer_product, sep='\n')
