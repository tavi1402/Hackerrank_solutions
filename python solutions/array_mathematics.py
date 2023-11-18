'''This code reads the dimensions of the matrices and then reads the elements of both matrices. 
It uses NumPy to perform various element-wise operations (addition, subtraction, multiplication, 
integer division, remainder, and exponentiation) on the matrices 'a' and 'b' and prints the results separately.'''

import numpy as np  # Import the NumPy library for array operations

# Read the dimensions of the matrices from the user as input.
n, m = map(int, input().split())

# Read the elements of matrices 'a' and 'b' from the user input. Each matrix is constructed as a NumPy array.
a = np.array([input().split() for _ in range(n)], dtype=int)
b = np.array([input().split() for _ in range(n)], dtype=int)

# Perform various mathematical operations on the matrices 'a' and 'b:
# - Addition: a + b
# - Subtraction: a - b
# - Element-wise multiplication: a * b
# - Element-wise integer division: a // b
# - Element-wise remainder: a % b
# - Element-wise exponentiation: a ** b
# Each result is printed on separate lines with 'sep='\n''.
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')


