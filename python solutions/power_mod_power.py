'''In this code, it reads three integers ('a', 'b', and 'm'), calculates 'c' as 'a' raised to the power of 'b' 
using math.pow(), and calculates 'd' as the remainder of 'c' divided by 'm'. Finally, it prints 'c' and 'd' as integers.'''

# Import the 'math' module to use mathematical functions.
import math

# Read three integers 'a', 'b', and 'm' from the user as input.
a = int(input())
b = int(input())
m = int(input())

# Calculate 'c' as 'a' raised to the power of 'b' using the 'math.pow()' function.
# This computes 'a' raised to the power 'b' and returns a floating-point result.
c = math.pow(a, b)

# Calculate 'd' as the remainder of 'c' divided by 'm'.
d = c % m

# Print 'c' and 'd', converting them to integers to remove the decimal part.
# The 'int()' function is used to convert a floating-point number to an integer.
print(int(c))
print(int(d))
