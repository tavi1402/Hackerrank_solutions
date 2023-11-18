'''this code reads a list of integers and checks two conditions: whether all the integers are positive and whether 
at least one string in the list is a palindrome. If both conditions are satisfied, it prints True; otherwise, 
it prints False.'''

# Read and discard an integer from the user's input.
_ = input()

# Read a space-separated string of integers from the user's input and split it into a list of strings.
n = input().split()

# Check two conditions using list comprehensions and the built-in functions 'all' and 'any':
# 1. 'all([int(i) > 0 for i in n])' checks if all integers in the list 'n' are greater than 0.
# 2. 'any([j == j[::-1] for j in n])' checks if at least one string in the list 'n' is a palindrome.
#    'j == j[::-1]' compares a string with its reverse to determine if it's a palindrome.

# The results of these two conditions are combined with 'and', meaning both conditions must be true for the final result to be 'True'.

# Print the final result, which is 'True' if all integers are positive and at least one string is a palindrome, 'False' otherwise.
print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))
