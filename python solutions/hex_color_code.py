'''the code reads a series of lines and uses a regular expression to extract hexadecimal color codes from each line. 
If any matches are found, they are printed, with each match on a new line. The regular expression pattern captures color 
codes that start with either 3 or 6 characters after the '#' symbol, followed by valid hexadecimal characters.'''
import re

# Iterate through the number of lines specified
for _ in range(int(input())):
    # Use re.findall() to find all matches of the regex pattern in the input line
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())

    # Check if there are any matches
    if matches:
        # Print the matches, separating them by a newline
        print(*matches, sep='\n')
