'''the code compiles a regular expression pattern to match valid decimal numbers (with an optional sign) and then 
checks if the input strings match this pattern. However, the results are not printed or displayed in this code snippet.'''

from re import match, compile

# Compile a regular expression pattern using the 're' module.
# The pattern '^[-+]?[0-9]*\.[0-9]+$' matches decimal numbers (with optional sign).
pattern = compile('^[-+]?[0-9]*\.[0-9]+$')

# Loop through each test case (as indicated by the range).
for _ in range(int(input())):
    # Read an input string from standard input and check if it matches the compiled pattern.
    # The 'pattern.match(input())' returns a match object if the input string matches the pattern.
    # If there's a match, the 'match' function returns a truthy value, and 'bool' converts it to a boolean value.
    # The result indicates whether the input string is a valid decimal number with an optional sign.
    is_valid = bool(pattern.match(input()))

# The code doesn't print or output the result, so there might be a missing print statement to display the results.
