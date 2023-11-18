'''The provided Python code uses the re.findall() function to find all occurrences of the specified 
regex pattern in the input string Test_String. The regex pattern is defined as r'(.)(?!\1)'. 
Let's break down the pattern:

- (.): This part captures any character (except for a newline) and places it in a capturing group.
- (?!\1): This is a negative lookahead assertion. It asserts that what immediately follows the captured 
    character is not the same character captured earlier. \1 refers to the first capturing group.

So, the pattern is looking for instances where a character is not followed by the same character in the 
input string.'''

import re

Regex_Pattern = r'(.)(?!\1)'

Test_String = input("Enter a string: ")

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches:", len(match))
