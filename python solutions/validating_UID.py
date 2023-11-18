'''this code checks if the input strings adhere to specific criteria and prints "Valid" if they do, or "Invalid" 
if any of the conditions are not satisfied. The code uses regular expressions and assertions to perform these checks.'''

import re  # Import the regular expression module

# Read the number of test cases from the user as input.
for _ in range(int(input())):
    u = ''.join(sorted(input()))  # Read an input string and sort its characters.

    try:
        # Check if there are at least two uppercase letters (A-Z).
        assert re.search(r'[A-Z]{2}', u)

        # Check if there are at least three consecutive digits (0-9).
        assert re.search(r'\d\d\d', u)

        # Check if the string contains only alphanumeric characters (letters and digits).
        assert not re.search(r'[^a-zA-Z0-9]', u)

        # Check if there are no repeated characters using a regular expression.
        assert not re.search(r'(.)\1', u)

        # Check if the length of the string is exactly 10 characters.
        assert len(u) == 10
    except:
        print('Invalid')  # If any of the conditions are not met, print 'Invalid'.
    else:
        print('Valid')  # If all conditions are met, print 'Valid'.
