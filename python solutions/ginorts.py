'''this code sorts the characters in the input string by their digit status, case status, and even-digit status, 
while maintaining the original order of characters with the same properties. The sorted characters are then 
printed as a single string.'''

# Read a string from standard input using the 'input()' function.
# The input string is then passed to the 'sorted()' function for sorting.
# The 'sorted()' function returns a sorted list of characters based on the provided key function.

# The key function specified in the 'sorted()' function is a lambda function.
# This lambda function calculates a sorting key for each character 'c' in the input string.

# The key function consists of three conditions that determine the order of sorting:
# 1. (c.isdigit() - c.islower()): Characters are sorted by whether they are digits, lowercase letters, or other characters.
#    - If 'c' is a digit, it gets a higher position (sorted first).
#    - If 'c' is a lowercase letter, it comes after digits (sorted next).
#    - If 'c' is neither a digit nor a lowercase letter, it comes last (sorted last).
# 2. (c in '02468'): Characters that are even digits ('02468') are sorted before others.
#    - Even digits are sorted first among the digits.
# 3. (c): For characters that have the same values according to the above conditions, they are sorted based on their original order.

# The sorted characters are joined into a single string using the 'join()' function, and the result is printed.
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
