'''this code allows you to enter a Python expression as a string, evaluates it, and prints the result using 
the print() function, making it compatible with both Python 2 and 3.'''

# Import the print_function from the __future__ module to enable Python 3-style printing.
from __future__ import print_function

# Read an input string from the user and evaluate it as a Python expression using eval().
# The result of the evaluation will be printed.
eval(input())
