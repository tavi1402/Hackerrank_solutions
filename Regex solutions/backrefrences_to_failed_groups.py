'''The provided regular expression (Regex_Pattern) is designed to match a specific pattern for a string:

- ^\d{2}: Matches the start of the string followed by two digits.
- (-?): Uses a capturing group to match an optional hyphen (-). The question mark (?) makes the hyphen optional.
- \d{2}: Matches two digits.
- \1: This is a backreference to the capturing group, ensuring that if a hyphen is present, it should be the same as the one captured earlier.
- \d{2}: Matches two digits.
- \1: Another backreference to the capturing group for consistency.
- \d{2}$: Matches two digits at the end of the string.

Here's the breakdown of the pattern:

- ^\d{2}: Start with two digits.
- (-?): Optionally match a hyphen and capture it.
- \d{2}\1\d{2}\1\d{2}: Match two digits, the captured hyphen (if any), two digits, the captured hyphen (if any), and two more digits.
- $: End of the string.

So, this regular expression is checking for a specific pattern of digits and hyphens in a string.'''

Regex_Pattern = r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$"  # Regular expression pattern

import re

# Input from the user
input_string = input()

# Use re.search to check if the pattern is present in the input string
result = re.search(Regex_Pattern, input_string)

# Convert the result to a boolean, print the lowercase representation
print(str(bool(result)).lower())

