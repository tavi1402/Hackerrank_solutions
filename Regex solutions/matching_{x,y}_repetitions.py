'''Explanation of the regular expression Regex_Pattern:

- ^: Asserts the start of the string.
- \d{1,2}: Matches one or two digits.
- [a-zA-Z]{3,}: Matches three or more consecutive characters, where each character must be a letter (uppercase or lowercase).
- \.{0,3}: Matches zero to three consecutive periods (dots).
- $: Asserts the end of the string.'''

# Define the regular expression pattern using raw string (r)
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'  # Do not delete 'r'.

# Import the regular expression module 're'
import re

# Prompt the user for input and check if it matches the pattern
# Convert the result to lowercase and print it
print(str(bool(re.search(Regex_Pattern, input()))).lower())
