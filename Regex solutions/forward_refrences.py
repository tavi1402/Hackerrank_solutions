'''The provided regular expression r'^(\2tic|(tac))+$' breaks down as follows:

- ^: Anchors the match at the beginning of the string.
- (: Starts a capturing group.
- \2: A backreference to the second capturing group (which is not defined in this context, so it doesn't refer 
    to anything specific).
- tic: Matches the literal characters "tic."
- |: Acts as an OR operator, allowing either the left or right side of the expression to match.
- (tac): Another capturing group that matches the literal characters "tac."
- ): Ends the capturing group.
- +: Specifies that the entire group, consisting of either "tic" or "tac," must appear one or more times.
- $: Anchors the match at the end of the string.

This regular expression is designed to match strings that consist of either the repeated sequence "tic" or 
the sequence "tac" repeated one or more times.'''

import re

# Define the regular expression pattern
regex_pattern = r'^(\2tic|(tac))+$'

# Take user input for the test string
test_string = input()

# Check if the test string matches the pattern using re.match
if re.match(regex_pattern, test_string):
    print("true")  # Print "true" if there is a match
else:
    print("false")  # Print "false" if there is no match
