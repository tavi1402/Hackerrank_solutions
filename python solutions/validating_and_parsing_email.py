'''this code reads a list of name-email pairs, checks if the email addresses are in a valid format according to the 
regular expression pattern, and prints the valid pairs. The regular expression pattern is designed to match email 
addresses enclosed in angle brackets < and >, with specific character and format requirements inside.'''

import re

# Define a regular expression pattern to match valid email addresses
pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'

# Read the number of name-email pairs to check
n = int(input())

# Iterate through each name-email pair
for _ in range(n):
    name, email = input().split(' ')
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        print(name, email)
