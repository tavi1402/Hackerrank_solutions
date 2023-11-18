'''Explanation of the regular expression Regex_Pattern:

- ^: Asserts the start of the string.
- [^\d]: Matches any character that is not a digit.
- [^aeiou]: Matches any character that is not a lowercase vowel.
- [^bcDF]: Matches any character that is not a lowercase 'b', 'c', 'D', or 'F'.
- [^\s]: Matches any character that is not a whitespace character.
- [^AEIOU]: Matches any character that is not an uppercase vowel.
- [^.,]: Matches any character that is not a period (.) or a comma (,).
- $: Asserts the end of the string.

So, this regular expression is designed to match strings that follow a specific pattern where each character in 
the string must not belong to certain specified sets for each position.'''

# Define the regular expression pattern using raw string (r)
Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'  # Do not delete 'r'.

# Import the regular expression module 're'
import re

# Prompt the user for input and check if it matches the pattern
# Convert the result to lowercase and print it
print(str(bool(re.search(Regex_Pattern, input()))).lower())
