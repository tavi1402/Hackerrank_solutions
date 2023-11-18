'''The provided code uses a regular expression (regex_pattern) to match a specific pattern for an input string 
(test_string). The pattern is designed to match strings that have the format "...............," where each "..." 
represents any three characters and each "...." represents a dot followed by three characters. The re.match() 
function is used to check if the entire string matches the pattern, and the result is converted to a boolean value 
(True if there is a match, False otherwise). Finally, the code prints the lowercase string representation of the match 
result.'''

regex_pattern = r"^...\....\....\....$"  # Regular expression pattern to match a specific format

import re

test_string = input()  # Get input from the user

match = re.match(regex_pattern, test_string) is not None  # Check if the entire string matches the pattern

print(str(match).lower())  # Print the lowercase string representation of the match result

# For example, if the input string is "abc.def.1234.5678," the output would be: True