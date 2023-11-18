'''
The provided Python code uses the re.findall() function to find all occurrences of the specified regex 
pattern in the input string Test_String. The regex pattern is defined as r'o(?=oo)'. Let's break down the pattern:

- o: Matches the character 'o'.
- (?=oo): This is a positive lookahead assertion. It asserts that what immediately follows the 'o' is 'oo', 
    but it does not include 'oo' in the match.

So, the pattern is looking for instances where 'o' is followed by 'oo' in the input string.'''

import re

Regex_Pattern = r'o(?=oo)'

Test_String = input("Enter a string: ")

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches:", len(match))
