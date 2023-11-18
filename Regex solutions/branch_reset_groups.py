'''The regular expression you provided is intended to match a pattern of digits separated by a hyphen (-), 
double hyphen (--), period (.), or colon (:). Let's break down the expression:

- ^: Asserts the start of the string.
- \d{2}: Matches exactly two digits.
- (: Begins a capturing group for the separator.
- -(?:--)?: Matches a hyphen (-) optionally followed by another hyphen (--). The (?:...) is a non-capturing group.
- |: Alternation, allowing the use of multiple separators.
- \.: Matches a period (.).
- |: Alternation.
- :: Matches a colon (:).
- ): Ends the capturing group.
- \d{2}: Matches exactly two digits.
- \1: Backreference to the first capturing group, ensuring that the separator is repeated.
- \d{2}: Matches exactly two digits.
- \1: Backreference to the first capturing group.
- \d{2}: Matches exactly two digits.
- $: Asserts the end of the string.

This regex will match strings like "12-34-56", "12.34.56", "12:34:56", "12--34--56", etc. The separators 
must be the same throughout the string. The backreference \1 ensures that the same separator is used consistently.'''

import re

# Define the regular expression pattern
regex_pattern = r"^\d{2}(-(?:--)?|\.|:)\d{2}\1\d{2}\1\d{2}$"

# Take user input for the test string
test_string = input()

# Check if the test string matches the pattern using re.match
if re.match(regex_pattern, test_string):
    print("true")  # Print "true" if there is a match
else:
    print("false")  # Print "false" if there is no match
