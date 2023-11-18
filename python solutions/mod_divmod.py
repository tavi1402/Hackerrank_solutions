'''The code reads two integers, 'A' and 'B,' and then performs integer division, calculates the remainder, 
and uses the divmod function to return both results in a tuple.'''

# Read two integers 'A' and 'B' from the user as input.
A = int(input())
B = int(input())

# Calculate integer division (floor division) of 'A' by 'B' and print the result.
# Integer division means dividing 'A' by 'B' and keeping only the whole number part of the quotient.
# For example, if A is 10 and B is 3, A // B will result in 3, as 10 divided by 3 is 3 with a remainder of 1.
print(A // B)

# Calculate the remainder of 'A' divided by 'B' and print the result.
# This is done using the modulus operator (%), which returns the remainder of the division.
# For example, with A = 10 and B = 3, A % B will result in 1, which is the remainder.
print(A % B)

# The divmod() function is a built-in Python function that takes two arguments and returns a tuple containing the result of integer division and the remainder.
# It's equivalent to (A // B, A % B), so it combines both division and remainder calculations.
# For example, with A = 10 and B = 3, divmod(A, B) will return (3, 1), representing the result of division (3) and the remainder (1).
print(divmod(A, B))
