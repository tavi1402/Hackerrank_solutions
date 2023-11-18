'''The provided regular expression (Regex_Pattern) is designed to match a specific pattern in a string. 
Here's the breakdown of the pattern:

- ^: Asserts the start of the string.
- \d: Matches any digit (0-9).
- \S{4}: Matches exactly four non-whitespace characters.
- \.: Matches a period (dot).
- $: Asserts the end of the string.

So, the overall pattern is seeking to match a string that starts with a digit, followed by exactly four non-whitespace 
characters, and ends with a period.'''

Regex_Pattern = r"^\d\S{4}\.$"  # Regular expression pattern

import re

# Input from the user
input_string = input()

# Use re.search to check if the pattern is present in the input string
result = re.search(Regex_Pattern, input_string)

# Convert the result to a boolean, print the lowercase representation
print(str(bool(result)).lower())

# For example, if the input string is "1abcd.", the output would be: True