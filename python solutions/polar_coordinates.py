'''In this code, the cmath module is used to work with complex numbers. It reads a complex number as a string, 
converts it to a complex number using complex(), calculates its absolute value using abs(), and calculates its 
phase angle using cmath.phase(). Finally, it prints both the absolute value and phase angle.'''

# Import the cmath module, which provides functions for complex number operations.
import cmath

# Read a complex number as input from the user and store it as a string.
n = input()

# Convert the input string to a complex number and calculate its absolute value (magnitude).
# Then, print the absolute value.
print(abs(complex(n)))

# Calculate the phase angle (argument) of the complex number and print it.
print(cmath.phase(complex(n)))
