'''This code uses NumPy to evaluate a polynomial function at a given value of 'x' '''

import numpy as np  # Import the NumPy library for array operations

# Read a list of space-separated coefficients for a polynomial from the user as input.
poly = [float(x) for x in input().split()]

# Read a single floating-point value 'x' from the user as input.
x = float(input())

# Evaluate the polynomial with the given coefficients at the value 'x' using `np.polyval(poly, x)`.
result = np.polyval(poly, x)

# Print the result, which is the value of the polynomial at 'x'.
print(result)
