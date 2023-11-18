'''let's break down the regular expression:

- ^: Asserts the start of the string.
- \d{2,}: Matches two or more digits.
- [a-z]*: Matches zero or more lowercase letters.
- [A-Z]*: Matches zero or more uppercase letters.
- $: Asserts the end of the string.

So, the regular expression is looking for strings that start with at least two digits, followed by zero or more lowercase letters, 
and zero or more uppercase letters, and nothing else until the end of the string.'''

# Define a regular expression pattern
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'  # Do not delete 'r'.

# Import the 're' module for regular expressions
import re

# Prompt the user for input and check if it matches the pattern
# Convert the boolean result to a string and print it in lowercase
print(str(bool(re.search(Regex_Pattern, input()))).lower())
