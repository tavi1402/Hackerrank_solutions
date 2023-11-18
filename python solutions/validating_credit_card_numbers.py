# Import the 're' module to work with regular expressions
import re

# Read the number of test cases (n) from the user
n = int(input())

# Loop through each test case
for t in range(n):
    # Read the credit card number as input and remove any extra spaces
    credit = input().strip()

    # Remove hyphens from the credit card number
    credit_removed_hyphen = credit.replace('-', '')

    # Assume the credit card is valid by default
    valid = True

    # Check if it's a 16-digit number that starts with 4, 5, or 6
    length_16 = bool(re.match(r'^[4-6]\d{15}$', credit))

    # Check if it's a 19-character number with the right pattern
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', credit))

    # Check if there are four consecutive identical digits (e.g., '1111')
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)', credit_removed_hyphen))

    # Check if it matches the pattern for either 16 or 19 characters
    if length_16 == True or length_19 == True:
        # If it does, further check for consecutive digits
        if consecutive == True:
            valid = False
    else:
        # If it doesn't match the initial patterns, it's invalid
        valid = False

    # If the credit card is still marked as valid, print 'Valid,' otherwise print 'Invalid'
    if valid == True:
        print('Valid')
    else:
        print('Invalid')
