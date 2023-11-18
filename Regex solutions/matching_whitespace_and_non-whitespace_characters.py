'''The provided regular expression (Regex_Pattern) is designed to match a pattern in a string. 
Here's the breakdown of the pattern:

- \S: Matches any non-whitespace character.
- \S\S: Matches two consecutive non-whitespace characters.
- \s: Matches any whitespace character (space, tab, newline).
- \S\S: Matches two consecutive non-whitespace characters.
- \s: Matches any whitespace character.
- \S\S: Matches two consecutive non-whitespace characters.

So, the overall pattern is seeking to match a sequence of two non-whitespace characters, followed by a 
whitespace character, another two non-whitespace characters, another whitespace character, and a final two 
non-whitespace characters.'''

Regex_Pattern = r"\S\S\s\S\S\s\S\S"  # Regular expression pattern

import re

# Input from the user
input_string = input()

# Use re.search to check if the pattern is present in the input string
result = re.search(Regex_Pattern, input_string)

# Convert the result to a boolean, print the lowercase representation
print(str(bool(result)).lower())

# For example, if the input string is "ab cd ef," the output would be: true