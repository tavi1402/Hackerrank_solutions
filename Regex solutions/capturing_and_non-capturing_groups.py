'''the code is checking if the substring 'ok' appears consecutively at least three times in the user input. 
If it does, it prints True; otherwise, it prints False.

Explanation:

- r'(ok){3,}': This is a raw string (indicated by the 'r' prefix) containing a regular expression pattern.
- (ok): Matches the substring 'ok'.
- {3,}: Specifies that the preceding group (in this case, '(ok)') must appear at least 3 or more times 
    consecutively.
'''
Regex_Pattern = r'(ok){3,}'  # Do not delete 'r'.

import re

# Take user input
user_input = input()

# Use re.search to check if the regular expression pattern is present in the input
match = re.search(Regex_Pattern, user_input)

# Print True if there is a match, False otherwise
print(str(bool(match)).lower())

