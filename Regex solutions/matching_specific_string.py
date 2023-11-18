'''The provided code uses a regular expression (Regex_Pattern) to find matches of the string "hackerrank" in the input 
string (Test_String). The re.findall() function is used to find all non-overlapping matches and store them in the 
variable match. Finally, the code prints the number of matches found.'''

Regex_Pattern = r'hackerrank'   # Regular expression pattern to match 'hackerrank'

import re

Test_String = input()  # Get input from the user

match = re.findall(Regex_Pattern, Test_String)  # Find all matches of the pattern in the input string

print("Number of matches:", len(match))  # Print the number of matches found

# For example, if the input string is "hackerrank is a platform for hackerrank challenges," the output would be: 2