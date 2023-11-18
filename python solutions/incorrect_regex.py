''' this code tests the validity of regular expression patterns for multiple test cases. 
If the compilation of the regular expression is successful, it prints True; otherwise, it prints False. 
The try and except blocks handle potential errors during the compilation process.'''

# Import the re module for regular expressions.
import re

# Read an integer T representing the number of test cases.
T = int(input())

# Iterate through each test case.
for _ in range(T):  
    try:
        # Try to compile a regular expression pattern from the user input.
        print(bool(re.compile(input())))
    except:
        # If compilation fails, print 'False'.
        print('False')
