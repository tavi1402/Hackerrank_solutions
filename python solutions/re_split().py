'''this code takes an input string and splits it into substrings using the regular expression pattern '[.,]+' 
(matching periods and commas). It then prints the resulting substrings on separate lines.'''

# Define a regular expression pattern 'regex_pattern'.
regex_pattern = r'[.,]+'  # 'r' before the string signifies a raw string, which is often used for regular expressions.

# Import the 're' module, which provides functions for working with regular expressions.
import re

# Read an input string from the user using the 'input()' function.
input_string = input()

# Use the 're.split()' function to split the input string based on the specified regular expression pattern.
# In this pattern, '[.,]+' matches one or more consecutive occurrences of periods (.) or commas (,).
# The 're.split()' function returns a list of substrings after splitting.

# Print the resulting substrings, joining them with newline characters ('\n').
# This effectively prints each substring on a separate line.
print("\n".join(re.split(regex_pattern, input_string)))
