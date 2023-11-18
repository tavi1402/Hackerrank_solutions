'''let's break down the regular expression pattern:

- ^: Asserts the start of the string.
- [Hh]: Matches either 'H' or 'h'.
- [Ii]: Matches either 'I' or 'i'.
- \s: Matches any whitespace character (space, tab, etc.).
- [^Dd]: Matches any character that is not 'D' or 'd'.

So, the regular expression is looking for a string that starts with "hi" (case-insensitive), 
followed by a space, and the character after that is not 'd' or 'D'.
'''

import re  # Import the regular expression module

n = int(input())  # Read the number of test cases from the user

for _ in range(n):  # Loop through each test case
    S = input()  # Read a string from the user for each test case
    
    # Check if the string S matches the specified regular expression pattern
    if re.search("^[Hh][Ii]\s[^Dd]", S):
        print(S)  # If the condition is met, print the string S
