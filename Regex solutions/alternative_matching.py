''' the code is checking if the input string represents one of the specified titles followed by an alphabetic 
name. If there is a match, it prints True; otherwise, it prints False.

Explanation:

- r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([a-zA-Z]+)$': This is a raw string (indicated by the 'r' prefix) containing a 
    regular expression pattern.
- ^: Anchors the match at the beginning of the string.
- (Mr\.|Mrs\.|Ms\.|Dr\.|Er\.): Matches one of the specified titles followed by a period. The titles are separated 
    by the | (OR) operator.
- ([a-zA-Z]+): Matches one or more alphabetic characters (both uppercase and lowercase) and captures them in a 
    group.
- $: Anchors the match at the end of the string.
'''

Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([a-zA-Z]+)$'  # Do not delete 'r'.

import re

# Take user input
user_input = input()

# Use re.search to check if the regular expression pattern is present in the input
match = re.search(Regex_Pattern, user_input)

# Print True if there is a match, False otherwise
print(str(bool(match)).lower())
