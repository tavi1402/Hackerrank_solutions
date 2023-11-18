'''Explanation:

- r'\b[aeiouAEIOU][a-zA-Z]*\b': This is a raw string (indicated by the 'r' prefix) containing a regular 
    expression pattern.
- \b: Word boundary assertion. Ensures that the pattern is found at the beginning or end of a word.
- [aeiouAEIOU]: Matches any single vowel (case-insensitive).
- [a-zA-Z]*: Matches any sequence of zero or more alphabetical characters (both uppercase and lowercase).
- \b: Another word boundary assertion.'''

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'    # Do not delete 'r'.

import re

# Take user input
user_input = input()

# Use re.search to check if the regular expression pattern is present in the input
match = re.search(Regex_Pattern, user_input)

# Print True if there is a match, False otherwise
print(str(bool(match)).lower())
