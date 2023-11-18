''' this code searches for all occurrences of the given substring in the main string and prints the starting and 
ending indices of these occurrences. If the substring is not found, it prints (-1, -1).'''

# Import the 're' module, which provides functions for working with regular expressions.
import re

# Read the main string from standard input.
string = input()

# Read the substring to search for in the main string.
substring = input()

# Compile the regular expression pattern using the substring.
pattern = re.compile(substring)

# Use 'pattern.search()' to find the first match of the substring in the main string.
match = pattern.search(string)

# Check if no match was found.
if not match:
    # If no match is found, print (-1, -1) to indicate that the substring is not present in the main string.
    print('(-1, -1)')

# If there is at least one match:
while match:
    # Print the starting and ending indices of the match using the 'start()' and 'end()' methods.
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    
    # Use 'pattern.search()' again to find the next occurrence, starting one character after the previous match.
    match = pattern.search(string, match.start() + 1)
