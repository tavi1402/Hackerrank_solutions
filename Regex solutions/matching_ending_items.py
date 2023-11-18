'''This regular expression, ^[a-zA-Z]*s$, is designed to match strings that end with the letter 's' 
(case-insensitive). Here's a breakdown of the expression:

- ^: Asserts the start of the string.
- [a-zA-Z]*: Matches zero or more occurrences of any alphabet letter (both lowercase and uppercase).
- s: Matches the literal letter 's'.
- $: Asserts the end of the string.

Therefore, the entire pattern ensures that the string must start with any combination of alphabet letters 
and end with the letter 's'.'''

import re

# Define the regular expression pattern
Regex_Pattern = r'^[a-zA-Z]*s$'

# Take user input for the test string
test_string = input()

# Check if the test string matches the pattern using re.search
if re.search(Regex_Pattern, test_string):
    print("true")  # Print "true" if there is a match
else:
    print("false")  # Print "false" if there is no match
