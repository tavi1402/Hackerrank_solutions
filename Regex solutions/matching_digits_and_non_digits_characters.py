'''The provided regular expression (Regex_Pattern) is designed to match a pattern in a string. 
Here's the breakdown of the pattern:

- \d: Matches any digit (0-9).
- \d\d: Matches two consecutive digits.
- (.): Uses parentheses for capturing groups. This captures any single character and stores it in a group.
- \d\d: Matches two consecutive digits.
- (.): Another capturing group for any single character.
- \d\d\d\d: Matches four consecutive digits.

So, the overall pattern is seeking to match two digits, followed by any character, two more digits, 
another character, and finally four digits.'''

Regex_Pattern = r"\d\d(.)\d\d(.)\d\d\d\d"  # Regular expression pattern

import re

# Input from the user
input_string = input()

# Use re.search to check if the pattern is present in the input string
result = re.search(Regex_Pattern, input_string)

# Convert the result to a boolean, print the lowercase representation
print(str(bool(result)).lower())

# For example, if the input string is "12-34-5678," the output would be: True