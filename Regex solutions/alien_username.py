'''This Python code uses the re (regular expression) module to check whether input strings follow a specific pattern. The pattern is defined as:

- Here's a breakdown of the regular expression:
- ^[_\.]: Matches the start of the string with either underscore or period.
- [0-9]+: Matches one or more numeric digits.
- [a-zA-Z]*: Matches zero or more alphanumeric characters.
- [_]?$: Matches an optional underscore at the end of the string.'''

import re

# Define the regular expression pattern
pattern = re.compile('^[_\.][0-9]+[a-zA-Z]*[_]?$')

# Take the number of test cases as input
n = int(input())

# Iterate through each test case
for i in range(n):
    # Take user input for the test string
    x = str(input())

    # Check if the test string matches the pattern using re.findall
    if len(re.findall(pattern, x)) != 0:
        print("VALID")
    else:
        print("INVALID")
