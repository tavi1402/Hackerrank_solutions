'''this code reads a list of phone numbers and checks if each one is valid by matching them against the regular 
expression pattern. If a phone number matches the pattern, it's considered valid, and 'YES' is printed; otherwise, 
'NO' is printed.'''

import re

# Read the number of phone numbers to check
n = int(input())

# Use a list comprehension to iterate through the input phone numbers
# and check if each one matches the regular expression pattern
[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(n)]
