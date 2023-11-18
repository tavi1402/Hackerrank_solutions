import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Iterate through words in the input string
    for x in s[:].split():
        # Capitalize the first letter of each word and replace in the string
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    # Open an output file for writing
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read a line of text from standard input
    s = input()

    # Call the solve function to modify the string
    result = solve(s)

    # Write the modified string to the output file with a newline
    fptr.write(result + '\n')

    # Close the output file
    fptr.close()
