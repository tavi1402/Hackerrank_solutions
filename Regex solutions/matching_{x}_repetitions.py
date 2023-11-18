'''Explanation of the regular expression Regex_Pattern:

- ^: Asserts the start of the string.
- [a-zA-Z02468]{40}: Matches exactly 40 characters, where each character must be either a lowercase letter, uppercase letter, or one of the digits {0, 2, 4, 6, 8}.
- [\s13579]{5}: Matches exactly 5 characters, where each character must be a whitespace character (\s), or one of the digits {1, 3, 5, 7, 9}.
- $: Asserts the end of the string.'''

# Define the regular expression pattern using raw string (r)
Regex_Pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'  # Do not delete 'r'.

# Import the regular expression module 're'
import re

# Prompt the user for input and check if it matches the pattern
# Convert the result to lowercase and print it
print(str(bool(re.search(Regex_Pattern, input()))).lower())
