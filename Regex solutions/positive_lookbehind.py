'''
The provided Python code uses the re.findall() function to find all occurrences of the specified regex 
pattern in the input string Test_String. The regex pattern is defined as r'(?<=[13579])\d'. 
Let's break down the pattern:

- (?<=[13579]): This is a positive lookbehind assertion. It asserts that what precedes the current position 
- in the string is any one of the digits 1, 3, 5, 7, or 9.
- \d: This part matches any digit (0-9).

So, the pattern is looking for digits that are preceded by an odd digit in the input string.'''

import re

Regex_Pattern = r'(?<=[13579])\d'

Test_String = input("Enter a string: ")

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches:", len(match))
