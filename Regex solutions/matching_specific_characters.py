'''Let's break down the regular expression pattern:

- ^[123]: Matches the start of the string and expects the first character to be either '1', '2', or '3'.
- [120]: Expects the second character to be '1', '2', or '0'.
- [xs0]: Expects the third character to be 'x', 's', or '0'.
- [30Aa]: Expects the fourth character to be '3', '0', 'A', or 'a'.
- [xsu]: Expects the fifth character to be 'x', 's', or 'u'.
- [.,]$: Expects the sixth and final character to be either '.' or ',' and marks the end of the string.

So, the pattern represents a specific combination of characters in a six-character string.'''

# Define the regular expression pattern using raw string (r)
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'  # Do not delete 'r'.

# Import the regular expression module 're'
import re

# Prompt the user for input and check if it matches the pattern
# Convert the result to lowercase and print it
print(str(bool(re.search(Regex_Pattern, input()))).lower())
