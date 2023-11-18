'''this code searches for the first repeated character (consecutive characters) in the input string and prints 
the repeated character. If no repeated character is found, it prints -1.'''

# Import the 're' module, which provides functions for working with regular expressions.
import re

# Read an input string from standard input using the 'input()' function.
input_string = input().strip()  # Remove leading and trailing whitespaces from the input string.

# Use 're.search()' to search for a pattern in the input string.
# The pattern '([a-zA-Z0-9])\1' matches any single alphanumeric character followed by itself.
# It captures the repeated character in a capturing group (inside parentheses).

m = re.search(r'([a-zA-Z0-9])\1', input_string)

# Check if a match was found.
if m:
    # If a match was found, print the repeated character.
    print(m.group(1))
else:
    # If no match was found, print -1 to indicate that there are no repeated characters.
    print(-1)
