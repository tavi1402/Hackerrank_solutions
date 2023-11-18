'''The regular expression pattern is designed to validate Roman numerals, ensuring they follow the standard rules, 
including subtractive notation (e.g., 'IV' for 4, 'IX' for 9, 'XL' for 40, 'XC' for 90, 'CD' for 400, and 'CM' for 900). 
If the input matches the pattern, the re.match() function returns a match object, making the entire expression True, 
indicating that the input is a valid Roman numeral. If there's no match, it returns False.'''

regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'    # Do not delete 'r'.

# Import the 're' module for regular expressions.
import re

# Use the 're.match()' function to check if the input matches the regex pattern.
# The 'bool()' function is used to convert the match result into a boolean (True or False).
print(str(bool(re.match(regex_pattern, input()))))
