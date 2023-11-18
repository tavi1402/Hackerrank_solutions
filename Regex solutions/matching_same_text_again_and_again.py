'''The provided regular expression (Regex_Pattern) is designed to match a specific pattern in a string. 
Here's the breakdown of the pattern:

([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S): This part defines a capturing group containing the following sequence:

- [a-z]: Matches a lowercase letter.
- \w: Matches any word character (alphanumeric + underscore).
- \s: Matches any whitespace character.
- \W: Matches any non-word character.
- \d: Matches any digit.
- \D: Matches any non-digit.
- [A-Z]: Matches an uppercase letter.
- [a-zA-Z]: Matches any letter (either lowercase or uppercase).
- [aeiouAEIOU]: Matches a vowel (either lowercase or uppercase).
- \S: Matches any non-whitespace character.
- \1: This part is a backreference to the first capturing group. It ensures that the same sequence is repeated.

So, the overall pattern is seeking to match a specific sequence followed by the same sequence repeated.'''

Regex_Pattern = r'([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S)\1'  # Regular expression pattern

import re

# Input from the user
input_string = input()

# Use re.search to check if the pattern is present in the input string
result = re.search(Regex_Pattern, input_string)

# Convert the result to a boolean, print the lowercase representation
print(str(bool(result)).lower())

# For example, if the input string is "ab #1?AZa$ab #1?AZa$", the output would be: True

