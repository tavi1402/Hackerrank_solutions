'''The provided regular expression (Regex_Pattern) is designed to match a pattern in a string. 
Here's the breakdown of the pattern:

- \w: Matches any word character (alphanumeric + underscore).
- \w\w\w: Matches three consecutive word characters.
- \W: Matches any non-word character.
- \w\w\w\w\w\w\w\w\w\w\w\w\w\w\w: Matches fifteen consecutive word characters.
- \W: Matches any non-word character.
- \w\w\w: Matches three consecutive word characters.

So, the overall pattern is seeking to match three word characters, followed by a non-word character, fifteen word 
characters, another non-word character, and a final three word characters.'''

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"  # Regular expression pattern

import re

# Input from the user
input_string = input()

# Use re.search to check if the pattern is present in the input string
result = re.search(Regex_Pattern, input_string)

# Convert the result to a boolean, print the lowercase representation
print(str(bool(result)).lower())

# For example, if the input string is "abc-abcdefghijklm-xyz," the output would be: true