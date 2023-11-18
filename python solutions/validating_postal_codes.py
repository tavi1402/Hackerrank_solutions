# Define a regular expression pattern for a 6-digit integer where the first digit is between 1 and 9
regex_integer_in_range = r"^[1-9][\d]{5}$"

# Define a regular expression pattern to find alternating repetitive digit pairs
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

# Import the 're' module for working with regular expressions
import re

# Read an input string from the user
P = input()

# Check if the input string matches the 'regex_integer_in_range' pattern and return True or False
integer_range_match = re.match(regex_integer_in_range, P)

# Find all alternating repetitive digit pairs in the input string and count them
alternating_pairs = re.findall(regex_alternating_repetitive_digit_pair, P)

# Check if the input string meets both conditions:
# 1. It matches the integer range pattern
# 2. It has fewer than 2 alternating repetitive digit pairs
# If both conditions are met, it will be True; otherwise, it will be False.
is_valid = bool(integer_range_match) and len(alternating_pairs) < 2

# Print whether the input string is valid or not (True or False)
print(is_valid)
