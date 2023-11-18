'''Explanation of the regular expression Regex_Pattern:

- ^: Asserts the start of the string.
- [a-z]: Matches any lowercase alphabetical character.
- [1-9]: Matches any digit from 1 to 9.
- [^a-z]: Matches any character that is not a lowercase alphabetical character.
- [^A-Z]: Matches any character that is not an uppercase alphabetical character.
- [A-Z]: Matches any uppercase alphabetical character.
- .*: Matches zero or more occurrences of any character (except for a newline). '''

# Define the regular expression pattern using raw string (r)
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z].*'  # Do not delete 'r'.

# Import the regular expression module 're'
import re

# Prompt the user for input and check if it matches the pattern
# Convert the result to lowercase and print it
print(str(bool(re.search(Regex_Pattern, input()))).lower())
