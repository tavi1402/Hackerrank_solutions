'''this code searches for substrings in the input string that contain at least two consecutive vowels, 
surrounded by consonants. It then prints these substrings on separate lines. If no such substrings are found, 
it prints -1.'''

# Import the 're' module, which provides functions for working with regular expressions.
import re

# Define a string of vowels and consonants.
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

# Use the 're.findall()' function to find all matches in the input string.
# The regular expression pattern is constructed to look for:
# - '(?<=[' + consonants + '])': A positive lookbehind for any consonant.
# - '([' + vowels + ']{2,})': Matches at least two consecutive vowels.
# - '(?=[' + consonants + '])': A positive lookahead for any consonant.
# The 'flags=re.I' argument makes the regular expression case-insensitive.

matches = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)

# Check if any matches were found.
if matches:
    # If matches were found, join and print them on separate lines.
    print('\n'.join(matches))
else:
    # If no matches were found, print -1 to indicate that there are no such substrings.
    print('-1')
