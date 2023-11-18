'''let's break down the regular expression:

- ^: Asserts the start of the string.
- \d+: Matches one or more digits.
- [A-Z]+: Matches one or more uppercase letters.
- [a-z]+: Matches one or more lowercase letters.
- $: Asserts the end of the string.

So, the regular expression is looking for strings that start with one or more digits, followed by one or more uppercase letters, 
and then one or more lowercase letters until the end of the string.'''

# Define a regular expression pattern
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'  # Do not delete 'r'.

# Import the 're' module for regular expressions
import re

# Prompt the user for input and check if it matches the pattern
# Convert the boolean result to a string and print it in lowercase
print(str(bool(re.search(Regex_Pattern, input()))).lower())
